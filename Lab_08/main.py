import check_input
import car
import motorcycle
import truck

def main():
    print("Rad Racer!")
    print("Choose a vehicle and race it down the track (player = 'P'). Slow down for obstacles ('O') or else you'll crash!")
    print("1. Lightning Car - a fast car (6-8 units). Special: Nitro Boost (1.5x speed)")
    print("2. Swift Bike - a speedy motorcycle (6-8 units). Special: Wheelie (2x speed but there's a chance you'll crash).")
    print("3. Behemoth Truck - a heavy truck (4-8 units). Special: Ram (2x speed and it smashes through obstacles).")

    c_track = "C--------------O------------------------------------------------------------O-----------------------"
    mc_track = "M------------------------------O--------------------------------O-----------------------------------"
    t_track = "T------------------------O-----------------------------O--------------------------------------------"

    player = check_input.get_int_range("Choose your vehicle [1-3]:", 1, 3)

    match player:
        case 1:
            print("You chose the Lightning Car!")
            p_track = c_track.replace("C", "P")
        case 2:
            print("You chose the Swift Bike!")
            p_track = mc_track.replace("M", "P")
        case 3:
            print("You chose the Behemoth Truck!")
            p_track = t_track.replace("T", "P")

    print("Lighning Car [Position - 0, Energy - 100]")
    print("Swift Bike [Position - 0, Energy - 100]")
    print("Behemoth Truck [Position - 0, Energy - 100]")
    if player == 1:
        print(p_track + "\n" + mc_track + "\n" + t_track)
    elif player == 2:
        print(p_track + "\n" + c_track + "\n" + t_track)
    elif player == 3:
        print(p_track + "\n" + c_track + "\n" + mc_track)

    # while player position < 100 (or 99(?)):
        # action = check_input.get_int_range("Choose action (1. Fast, 2. Slow, 3. Special Move):", 1, 3)
        # move player appropriate distance
        # move opponents
        # if player hits an obstacle:
            # print(user hit an obstacle and crashed)
        # print out opponent status/movements
        # update map



    
main()