import check_input
import car
import motorcycle
import truck
import random

def main():

    # create a 2d list with three racetracks
    rows, cols = (3, 100)
    racetracks = [['-' for i in range(cols)] for j in range(rows)]
    # c_track = "C--------------O------------------------------------------------------------O-----------------------"
    # mc_track = "M------------------------------O--------------------------------O-----------------------------------"
    # t_track = "T------------------------O-----------------------------O--------------------------------------------"


    # randomly place 2 obstacles into each list
    elements = 0
    for row_index, track_row in enumerate(racetracks):
        while elements != 2:
            replace_with_zero = random.randint(2, 99)
            racetracks[row_index][replace_with_zero] = '0'
            elements += 1
        elements = 0

    # construct a list of the three vehicle objects
    racers = [car.Car(), motorcycle.Motorcycle(), truck.Truck()]
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('O') or else you'll crash!")
    print(f"1. {racers[0].description_string()}")
    print(f"2. {racers[1].description_string()}")
    print(f"3. {racers[2].description_string()}")
    

    player = check_input.get_int_range("Choose your vehicle (1-3):", 1, 3)
    """
    print("Lighning Car [Position - 0, Energy - 100]")
    print("Swift Bike [Position - 0, Energy - 100]")
    print("Behemoth Truck [Position - 0, Energy - 100]")
    if player == 1:
        print(p_track + "\n" + mc_track + "\n" + t_track)
    elif player == 2:
        print(p_track + "\n" + c_track + "\n" + t_track)
    elif player == 3:
        print(p_track + "\n" + c_track + "\n" + mc_track)
    """

    # while player position < 100 (or 99(?)):
        # action = check_input.get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move):", 1, 3)
        # move player appropriate distance
        # move opponents
        # if player hits an obstacle:
            # print(user hit an obstacle and crashed)
        # print out opponent status/movements
        # update map



    
main()