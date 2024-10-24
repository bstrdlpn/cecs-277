import check_input
import hero
import fire_dragon
import flying_dragon
import flying_fire_dragon

def main():
    """
    Construct a Hero object and then create a list that contains one of each of the
    dragons (FireDragon, FlyingDragon, FlyingFireDragon,). Present a menu that allows the user to
    choose which dragon to attack, and then another menu that gives them the option of attacking
    with a sword or an arrow. Call the hero’s attack method on the dragon they chose and display
    the attack message returned. If the user defeats the dragon (hp is 0), then remove that dragon
    from the list. Then choose a random (surviving) dragon that will attack the user, and randomly
    choose either a basic or special attack and display the attack message returned. Repeat the
    attacks until the user defeats all three dragons, or until the hero is knocked out. Check all input
    for validity.
    """
    
    # construct a Hero object
    print('What is your name, challenger?')
    name = input()
    print()
    player = hero.Hero(name, 50)
    print()

    # create list with three dragon objects
    dragons = [fire_dragon.FireDragon, flying_dragon.FlyingDragon, flying_fire_dragon.FlyingFireDragon]

    print(f"Welcome to dragon training, {name}")
    print('You must defeat 3 dragons')
    print()

    # main game loop
    # loop continues while list is populated
    while dragons:
        print(player)
        for index, dragon in enumerate(dragons):
            print(f"{index+1}. {str(dragon)}")
        attack_dragon = check_input.get_int_range('Choose a dragon to attack: ', 1, len(dragons))
        attack_dragon -= 1

        print('Attack with:')
        print('1. Sword (2 D6)')
        print('2. Arrow (1 D12)')
        attack = check_input.get_int_range('Enter weapon: ', 1, 2)

        if attack == 1:
            player.basic_attack(dragons[attack_dragon])
        else:
            player.special_attack(dragons[attack_dragon])
        
        if dragons[attack_dragon].hp == 0:
            del dragons[attack_dragon]
            # randomly select another dragon to attack
        #else:
            # that dragon attacks
main()