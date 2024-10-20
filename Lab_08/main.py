import check_input
import car
import motorcycle
import truck
import random

"""
Christina Hipolito, Long Nguyen
10/17/2024

Lab 08 - Rad Racer

User must choose a vehicle from a set of choices and then race against the 
remaining ones. 
"""

def create_tracks(num_racers, track_length):
    """
    Create racetracks, returns 2D list of tracks

    :param num_racers: int type; number of vehicles racing
    :param track_length: int type; total length of the track

    :returns: list type; 2D list of rows=racers, col=track length
    """

    rows, cols = (num_racers, track_length)
    tracks = [['-' for i in range(cols)] for j in range(rows)]
    return tracks

def insert_element(tracks, player_index = None, position=None): 
    """
    Randomly inserts '0' elements into the racetrack, OR if provided position data,
    insert '*' into position.

    :param tracks: list type; racetrack(s) to insert obstacles into
    :param player_index: int type; index of player in tracks list
    :param position: int type; position of element to replace, OPTIONAL
    
    :returns: list of tracks with elements inserted
    """
    # if optional parameters none (we are creating the tracks):
    if position is None:
        inserted_obstacles = 0
        # outer loop indexes into the racetrack list
        for row_index, track in enumerate(tracks):
            # inner loop replaces a rand element with a zero
            # after reqwuired number of obstacles inserted, break inner loop
            while inserted_obstacles != 2:
                # magic constants for now, haven't figured out how to parametrize
                replace_with_zero = random.randint(2, 99)
                tracks[row_index][replace_with_zero] = '0'
                inserted_obstacles += 1
            inserted_obstacles = 0
    # if the optional parameters have values, replace with *
    else:
        tracks[player_index][position] = '*'

    return tracks

def print_state(vehicles, tracks):
    """
    Prints state of vehicles and tracks
    
    :param vehicles: list type; list of vehicle objects
    :param tracks: list type; 2D list of racetracks 
    """

    for vehicle in vehicles:
        print(vehicle)
    for index, track in enumerate(tracks):
        print(''.join(tracks[index]))

def take_action():
    """
    Ask the user to select an action and return it.

    :returns: int type; action that user takes
    """

    choice = check_input.get_int_range('Choose action (1. Fast, 2. Slow, 3. Special Move): ', 1, 3)

    return choice

def distance_to_obstacle(vehicles, tracks, index):
    """
    Get distance to the next obstacle

    :param vehicles: list type; list of vehicle objects
    :param tracks: list type; racetracks list with inserted obstacles
    :param index: the index to check (which track/vehicle to check)

    :returns: None or int representing distance
    """
    position = vehicles[index].position
    dist = None
    found_first_obstacle = False

    for list_index, element in enumerate(tracks[index]):
        if element == '0':
            # position of the vehicle is before the first obstacle, get index, break loop
            if position < list_index:
                dist = list_index - position
                break
            elif not found_first_obstacle:
                found_first_obstacle = True
                dist = list_index - position

    return dist if dist is not None and dist > 0 else None

def cpu_take_action(vehicles, tracks, index):
    """Calculate the move for the CPU."""
    cpu_roll = random.randrange(1, 100)

    if 1 <= cpu_roll <= 30:
        print(vehicles[index].fast(distance_to_obstacle(vehicles, tracks, index)))
    elif 31 <= cpu_roll <= 70:
        print(vehicles[index].slow(distance_to_obstacle(vehicles, tracks, index)))
    else:
        print(vehicles[index].special_move(distance_to_obstacle(vehicles, tracks, index)))


def calculate_player_move(vehicles, tracks, index, choice):
    """Calculate the move for the player."""

    if choice == 1:
        print(vehicles[index].fast(distance_to_obstacle(vehicles, tracks, index)))
    # 2 = slow
    elif choice == 2:
        print(vehicles[index].slow(distance_to_obstacle(vehicles, tracks, index)))
    # 3 = special move
    elif choice == 3:
        print(vehicles[index].special_move(distance_to_obstacle(vehicles, tracks, index)))


def main():

    # win placement
    win_place = []

    # create a 2d list with three racetracks
    racetracks = create_tracks(3, 100)

    # randomly place 2 obstacles into each list
    racetracks = insert_element(racetracks)

    # construct a list of the three vehicle objects
    racers = [car.Car(), motorcycle.Motorcycle(), truck.Truck()]
    # track index position, this is for racers
    indexes = [0, 1, 2]
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('O') or else you'll crash!")
    print(f"1. {racers[0].description_string()}")
    print(f"2. {racers[1].description_string()}")
    print(f"3. {racers[2].description_string()}")
    
    player_index = check_input.get_int_range("Choose your vehicle (1-3):", 1, 3) - 1
    indexes.remove(player_index)
    cpu_1_index, cpu_2_index = random.sample(indexes, 2)
    
    racetracks[player_index][0] = 'P'
    racetracks[cpu_1_index][0] = racers[cpu_1_index].initial
    racetracks[cpu_2_index][0] = racers[cpu_2_index].initial

    # while any vehicles < 99
    while racers[player_index].position < 99 or racers[cpu_1_index].position < 99 or racers[cpu_2_index].position < 99:
        # print the state
        print()
        print_state(racers, racetracks)

        # take player action:
        if str(racers[player_index]) not in win_place:
            player_pos = racers[player_index].position
            choice = take_action()
            print()
            calculate_player_move(racers, racetracks, player_index, choice)
            if racers[player_index].position >= 99:
                win_place.append(str(racers[player_index]))
                insert_element(racetracks, player_index, player_pos)
                racetracks[player_index][99] = 'P'
            else:
                insert_element(racetracks, player_index, player_pos)
                racetracks[player_index][racers[player_index].position] = 'P'
      

        if str(racers[cpu_1_index]) not in win_place:
            #take cpu_1 action
            current_position = racers[cpu_1_index].position
            cpu_take_action(racers, racetracks, cpu_1_index)
            if racers[cpu_1_index].position >= 99:
                insert_element(racetracks, cpu_1_index, current_position)
                win_place.append(str(racers[cpu_1_index]))
                racetracks[cpu_1_index][99] = racers[cpu_1_index].initial
            else:
                insert_element(racetracks, cpu_1_index, current_position)
                racetracks[cpu_1_index][racers[cpu_1_index].position] = racers[cpu_1_index].initial

        if str(racers[cpu_2_index]) not in win_place:
        #take cpu_1 action
            current_position = racers[cpu_2_index].position
            cpu_take_action(racers, racetracks, cpu_2_index)
            if racers[cpu_2_index].position >= 99:
                insert_element(racetracks, cpu_2_index, current_position)
                win_place.append(str(racers[cpu_2_index]))
                racetracks[cpu_2_index][99] = racers[cpu_2_index].initial
            else:
                insert_element(racetracks, cpu_2_index, current_position)
                racetracks[cpu_2_index][racers[cpu_2_index].position] = racers[cpu_2_index].initial


    print_state(racers, racetracks)
    print(f"1st place: {win_place[0]}")
    print(f"2nd place: {win_place[1]}")
    print(f"3rd place: {win_place[2]}")
    
main()