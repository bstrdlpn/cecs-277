"""
Long Nguyen, Christina Hipolito
9/19/24

Treasure Hunt Game:
User navigates a map using WASD to find 7 hidden treasures while avoiding
traps. If the user gets caught in a trap they 
"""

def read_map():
    """
    Read contents of 'map.txt' and return a list of lists.
    """
    
    map = []

    # map.txt has char delimited a ' '
    with open("map.txt", 'r') as file:
        for row in file:
            sublist = row.split()
            map.append(sublist)

    return map


def display_map(map, player):
    """
    Display the player's position on the map.

    :param map:     2D list, map read from read_map()
    :param player:  list, player coordinates
    :returns:       Console display of map, with player position
    """

    # In each row, get the index number of the element
    for x, sublist in enumerate(map):
        # In each column get the index number of the element
        for y, char in enumerate(sublist):
            # If the player coord matches, display 'P'
            if x == player[0] and y == player[1]:
                print('P', end=' ')
            else:
                print(char, end=' ')
        print()


def move_player(player, dir, upper_bound):
    """
    moves the player in the selected direction (W=up, A=left, S=down, D=right).
    The boundaries of the map are between 0-upper_bound. Check that the location 
    that the user is trying to move to isn't out of bounds. If it isn't, then 
    update the user's location by changing the row and column values in the 
    location list by adding or subtracting 1 to the row or column (depending on 
    the direction they moved), otherwise, display an error message and do not 
    update the user's location.
    """
    # moves
    W = [0, -1]
    A = [-1, 0]
    S = [1, 0]
    D = [0, 1]

    try_move = []
    try_move += player

    if dir == 'W':
        try_move[1] += W[1]
    elif dir == 'A':
        try_move[0] += A[0]
    elif dir == 'S':
        try_move[0] += S[0]
    else:
        try_move[1] += D[1]

    if (0 < try_move[0] < upper_bound) and (0 < try_move[1] < upper_bound):
        return try_move
    else:
        print('You cannot move that direction.')
        return player
    
    
def count_treasures(map, player, upper_bound):
    """
    iterates through the surrounding spaces of the user's current location. 
    Keep a count of the number of treasures (T'), and traps ('X') that are in 
    those spaces. Return the two counts.
    """
    pass

def main():
    """
    Creates a loop that continues until the player quits. [insert rest of description]
    """
    map = read_map()
    player_map = [
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.']
    ]

    # initial player position at top-left of 'map'
    player = [0, 0]
    # map boundary
    upper_bound = len(map)

    print("Treasure Hunt!")
    print("""
          Find all 7 treasures without getting caught in a trap. Look around to 
          spot nearby traps and treasures.""")
    while True:
        display_map(map, player)
        dir = input("Enter Direction [WASD or L to Look around (hint) or Q to quit]: ").upper()
        if (len(dir) == 1) and (dir.isalpha()):
            if dir == ('W' or 'A' or 'S' or 'D'):
                move_player(player, dir, upper_bound)
                # if movement is invalid:
                    # print("You cannot move in that direction.")
                # if player falls in a trap:
                    # print("You were caught in a trap!")
                
                count_treasures_traps(map, player, upper_bound)
                # if all treasures were found:
                    # print("You found all the treasure!")
                    # break
            
            elif dir == 'L':
                "Look around for traps and treasures"
            
            elif dir == 'Q':
                print("Exiting. Thank you for playing!")
                exit()
        else:
            print("Invalid input.")

    print("Game Over!")
main()