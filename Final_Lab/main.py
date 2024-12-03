import check_input
import puppy

def main():
    """
    Construct a puppy object and then display a menu that allows the user to play with
    or feed the puppy. Display the puppy’s reaction to the user’s choice. Repeat until the
    user chooses to quit.
    """
    p = puppy.Puppy()

    print("Congratulations on your new puppy!")
    while True:
        print("What would you like to do?")
        print("1. Feed the puppy\n2. Play with the puppy\n3. Quit")
        option = check_input.get_int_range("",1,3)
        match option:
            case 1: # Feed the puppy
                print(p.give_food())
            case 2: # Play with the puppy
                print(p.throw_ball())
            case 3: # Quit
                break
main()