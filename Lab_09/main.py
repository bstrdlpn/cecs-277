import check_input
import random
import hero
import fire_dragon
import flying_dragon
import flying_fire_dragon

def main():
    """
    Construct a Hero object and then create a list that contains one of each of the
    dragons (FireDragon, FlyingDragon, FlyingFireDragon,). Present a menu that allows the user to
    choose which dragon to attack, and then another menu that gives them the option of attacking
    with a sword or an arrow. Call the hero's attack method on the dragon they chose and display
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
    dragons = [
    fire_dragon.FireDragon('Gronkle', 15, 3),
    flying_dragon.FlyingDragon('Timberjack', 10, 3),
    flying_fire_dragon.FlyingFireDragon('Deadly Nadder', 20, 2)
]

    print(f"Welcome to dragon training, {name}")
    print('You must defeat 3 dragons')
    print()

    # main game loop
    # loop continues while list is populated
    while dragons:
        print(player)
        for index, dragon in enumerate(dragons):
            print(f"{index+1}. {dragon}")
        attack_dragon = check_input.get_int_range('Choose a dragon to attack: ', 1, len(dragons))
        attack_dragon -= 1

        print('Attack with:')
        print('1. Sword (2 D6)')
        print('2. Arrow (1 D12)')
        attack = check_input.get_int_range('Enter weapon: ', 1, 2)

        if attack == 1:
            print(player.basic_attack(dragons[attack_dragon]))
        else:
            print(player.special_attack(dragons[attack_dragon]))

        dragon_attack = random.randint(1, 2)
        
        if dragons[attack_dragon].hp == 0:
            del dragons[attack_dragon]
            if len(dragons) == 0:
                print(f"Congratulations, {name} ! You have defeated all of the dragons!")
                break
            else:
                dr = random.choice(dragons)
                if dragon_attack == 1:
                    print(dr.basic_attack(player))
                else:
                    print(dr.special_attack(player))
        else:
            if dragon_attack == 1:
                print(dragons[attack_dragon].basic_attack(player))
            else:
                print(dragons[attack_dragon].special_attack(player))
        
        if player.hp == 0:
            print("Aww... You failed to defeat the dragons and have failed the trial.")
main()