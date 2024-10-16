import check_input
import car
import motorcycle
import truck
import random

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

def insert_element(tracks, position=None): 
    """
    Randomly inserts '0' elements into the racetrack, OR if provided position data,
    insert '*' into position.

    :param tracks: list type; racetrack(s) to insert obstacles into
    :param position: tuple type; position of element to replace, OPTIONAL
    
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
    # if the optional has a value, replace with *
    else:
        row, col = position
        tracks[row][col] = '*'

    return tracks

def print_state_take_action(vehicles, tracks):
    """
    Print the state of the vehicle objects, print track state, 
    and return the selected action.

    :param vehicles: list type; list of vehicle objects
    :param tracks: list type; 2D list of racetracks

    :returns: int type; action that user takes
    """

    for vehicle in vehicles:
        print(vehicle)
    for index, track in enumerate(tracks):
        print(''.join(tracks[index]))
    choice = check_input.get_int_range('Choose action (1. Fast, 2. Slow, 3. Special Move): ', 1, 3)

    return choice


def main():

    # win placement
    win_place = []

    # create a 2d list with three racetracks
    racetracks = create_tracks(3, 100)
    # c_track = "C--------------O------------------------------------------------------------O-----------------------"
    # mc_track = "M------------------------------O--------------------------------O-----------------------------------"
    # t_track = "T------------------------O-----------------------------O--------------------------------------------"


    # randomly place 2 obstacles into each list
    racetracks = insert_element(racetracks)


    # construct a list of the three vehicle objects
    racers = [car.Car(), motorcycle.Motorcycle(), truck.Truck()]
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('O') or else you'll crash!")
    print(f"1. {racers[0].description_string()}")
    print(f"2. {racers[1].description_string()}")
    print(f"3. {racers[2].description_string()}")
    
    player = check_input.get_int_range("Choose your vehicle (1-3):", 1, 3)

    # match case statement inserts player into desired racetrack
    match player:
        case 1:
            racetracks[0][0] = 'P'
            racetracks[1][0] = racers[1].initial
            racetracks[2][0] = racers[2].initial
        case 2:
            racetracks[0][0] = racers[0].initial
            racetracks[1][0] = 'P'
            racetracks[2][0] = racers[2].initial
        case 3:
            racetracks[0][0] = racers[0].initial
            racetracks[1][0] = racers[1].initial
            racetracks[2][0] = 'P'
        case _:
            # because of our get_int_range for player, i don't think we get here
            pass
        
    choice = print_state_take_action(racers, racetracks)
    
    # while all vehicles < 99
    while racers[0].position or racers[1].position or racers[2].position < 99:
        pass
        # print the state and take action

        # move player appropriate distance AND save previous position (to update map with *)

        # move opponents AND save previous position (to update map with *)

        # print player state/moves
        # print out opponent status/moves

        # IF vehicle has reached end, assign win placement (maybe list?)
        
        # update map



    
main()