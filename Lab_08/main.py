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

def insert_obstacles(tracks, obstacles, start, end):
    """
    Randomly insert 2 obstacles into the racetrack.

    :param tracks: list type; racetrack(s) to insert obstacles into
    :param start: int type; start index
    :param end: int type; end index
    
    :returns: list of tracks with obstacles inserted.
    """
    
    inserted_obstacles = 0
    # outer loop indexes into the racetrack list
    for row_index, track in enumerate(tracks):
        # inner loop replaces a rand element with a zero
        # after reqwuired number of obstacles inserted, break inner loop
        while inserted_obstacles != 2:
            replace_with_zero = random.randint(start + 1, end - 1)
            tracks[row_index][replace_with_zero] = '0'
            inserted_obstacles += 1
        inserted_obstacles = 0

    return tracks

def main():

    # create a 2d list with three racetracks
    racetracks = create_tracks(3, 100)
    # c_track = "C--------------O------------------------------------------------------------O-----------------------"
    # mc_track = "M------------------------------O--------------------------------O-----------------------------------"
    # t_track = "T------------------------O-----------------------------O--------------------------------------------"

    # randomly place 2 obstacles into each list
    racetracks = insert_obstacles(racetracks, 2, 0, 99)

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
            print(''.join(racetracks[0]))
        case 2:
            racetracks[1][0] = 'P'
            print(''.join(racetracks[1]))
        case 3:
            racetracks[2][0] = 'P'
            print(''.join(racetracks[2]))
        case _:
            # because of our get_int_range for player, i don't think we get here
            pass

    # while player position < 100 (or 99(?)):
        # action = check_input.get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move):", 1, 3)
        # move player appropriate distance
        # move opponents
        # if player hits an obstacle:
            # print(user hit an obstacle and crashed)
        # print out opponent status/movements
        # update map



    
main()