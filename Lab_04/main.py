"""
Long Nguyen, Christina Hipolito
09/19/24

Treasure Hunt Game:
User navigates a map using WASD to find 7 hidden treasures while avoiding
traps. The user can receive a hint that will tell them the number of treasures
and traps nearby. If the user finds all seven treasures, they win. If they run
into any traps, they lose.
"""

def read_map():
    """
    Read contents of 'map.txt' and return it as a list.

    :return map:    list, 2D list of map from text file
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

    :param map:     2D list
    :param player:  list, player coordinates
    :returns:       Console display of map, with player position
    """

    # In each row, get the index number of the element
    for row, sublist in enumerate(map):
        # In each column get the index number of the element
        for column, char in enumerate(sublist):
            # If the player coord matches, display 'P'
            if row == player[0] and column == player[1]:
                print('P', end=' ')
            else:
                print(char, end=' ')
        print()


def move_player(player, dir, upper_bound):
    """
    Move the player in the selected direction.

    :param player:      list, player (x, y) coordinates 
    :param dir:         char, W=up, A=left, S=down, D=right
    :param upper_bound: int, upper range where 0<= xy coords <= upper_bound

    :returns:           list, player coords
    """
    # moves
    W = [-1, 0]
    A = [0, -1]
    S = [1, 0]
    D = [0, 1]

    try_move = player.copy()

    if dir == 'W':
        try_move[0] += W[0]
    elif dir == 'A':
        try_move[1] += A[1]
    elif dir == 'S':
        try_move[0] += S[0]
    elif dir == 'D':
        try_move[1] += D[1]

    if (0 <= try_move[0] < upper_bound) and (0 <= try_move[1] < upper_bound):
        player = try_move.copy()
        return player
    else:
        print('You cannot move that direction.')
        return player
    
    
def count_treasures_traps(map, player, upper_bound):
    """
    Iterate through spaces adjacent to the player, return a count of treasures
    and traps.

    :param map:         list, contains locations of treasures and traps
    :param player:      list, contains player xy coords
    :param upper_bound: int, upper range where 0<= xy coords <= upper_bound

    :return count_treasure: int, number of treasures near player 
    :return count_trap:     int, number of traps near player
    """   
    search_direction = [[0, -1], [-1, 0], [0, 1], [1, 0], # up, left, right, down
                        [-1, -1], [1, -1], [-1, 1], [1,1]] # diagonal 
    row, column = player.copy()
    points_of_interest = []
    count_treasure = 0
    count_trap = 0

    # iterate through search direction list, get xy coords for adjacent squares
    for dx, dy in search_direction:
        search_x = row + dx
        search_y = column + dy

        # if within map bounds, element == char in map[row][column]
        if 0 <= search_x < upper_bound and 0 <= search_y < upper_bound:
            element = map[search_x][search_y]
            # if the element is a treasure or trap, append it
            if element in ['T', 'X']:
                points_of_interest.append(element)
    
    for element in points_of_interest:
        if element == 'T':
            count_treasure += 1
        elif element == 'X':
            count_trap += 1

    return count_treasure, count_trap


def main():
    """
    Creates a loop that continues until the player quits. [insert rest of description]
    """
    # map that contains the locations of the treasures and traps
    map = read_map()

    # map that the player will see when display_map is called
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
    
    past_positions = [[0,0]]

    # map boundary, square so len(map) gives us rows and columns
    upper_bound = len(map)
    remaining_treasure = 7

    print("Treasure Hunt!")
    print('Find all 7 treasures without getting caught in a trap. Look around to spot nearby traps and treasures.')
    while True:
        display_map(player_map, player)
        dir = input("Enter Direction [WASD or L to Look around (hint) or Q to quit]: ").upper()

        # validate player input
        if len(dir) == 1 and dir.isalpha():
            if dir in ['W', 'A', 'S', 'D']:
                player = move_player(player, dir, upper_bound)
                row, column = player.copy()
                
                # player falls into a trap
                if map[row][column] == 'X':
                    print("You were caught in a trap!")
                    if 7 - remaining_treasure == 1:
                        print(f"You found {7 - remaining_treasure} treasure.")
                    else:
                        print(f"You found {7 - remaining_treasure} treasures.")
                    display_map(player_map, player)
                    print('Game Over!')
                    break
                
                # player found a treasure
                if map[row][column] == 'T':
                    if player not in past_positions:
                        past_positions.append(player)
                        print('You found treasure!')
                        remaining_treasure -= 1
                        player_map[row][column] = 'T'
                    else:
                        continue
                    if remaining_treasure == 1:
                        print(f"There is {remaining_treasure} treasure remaining")
                    elif remaining_treasure > 1:
                        print(f"There are {remaining_treasure} treasures remaining")
                if remaining_treasure == 0:
                    print('You found all the treasures!')
                    break

            # player looks around
            elif dir == 'L':
                treasures, traps = count_treasures_traps(map, player, upper_bound)
                if treasures == 1:
                    print(f"You detect {treasures} treasure nearby.")
                else:
                    print(f"You detect {treasures} treasures nearby.")
                if traps == 1 and player_map[row][column] != 'T':
                    print(f"You detect {traps} trap nearby.")
                    player_map[row][column] = 1
                elif player_map[row][column] != 'T':
                    print(f"You detect {traps} traps nearby.")
                    player_map[row][column] = traps
            
            # player quits
            elif dir == 'Q':
                print("Exiting. Thank you for playing!")
                if 7 - remaining_treasure == 1:
                    print(f"You found {7 - remaining_treasure} treasure.")
                else:
                    print(f"You found {7 - remaining_treasure} treasures.")
                exit()

            # char input is invalid
            else:
                print('Invalid input - enter WASD, L, or Q')
        
        # Needed to catch if player enters something not alpha
        else:
            print("Invalid input - enter a letter")

main()