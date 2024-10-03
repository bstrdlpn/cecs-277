import check_input
import player


def take_turn(player):
    """roll the player’s dice, display the dice, check for and display any win
    types (pair, series, three-of-a-kind), and display the updated score"""
    d1 = p.die.Die()
    d2 = p.die.Die()
    d3 = p.die.Die()

    # p.roll_dice(self)
    # p.str(self)
    print(str(d1) + " " + str(d2) + " " + str(d3))

    #pass

def main():
    p = player.Player


    print("-Yahtzee-")
    take_turn(player)
    #while True:
        # 
        # yn = get_yes_no("Play again? (Y/N): ")
        # if yn == False:
            # break
        # else:
            # continue

    print("Game Over.") 

    #score = p.get_points(self)
    #print("Final Score = " + score)
    main()