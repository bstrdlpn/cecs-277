import hero
import enemy
import map
import check_input

def read_map(): # move into map
    """
    Read contents of 'map.txt' and return it as a list.

    :return map:    list, 2D list of map from text file
    """
    
    map = []

    # map.txt has char delimited a ' '
    with open("map-1.txt", 'r') as file:
        for row in file:
            sublist = row.split()
            map.append(sublist)

    return map
    
def move_player(player, dir, upper_bound): # move into hero
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

def main():
    h = hero.Hero()
    e = enemy.Enemy()
    m = map.Map()

    player_name = input("What is your name, traveler?: ").capitalize()
    print(player_name)
    # print player hp
    m.show_map(player)
    print("Where would you like to go? [North = up, South = down, East = right, and West = left]")
    direction = check_input.get_int_range("1. Go North\n2. Go South\n3. Go East\n4. Go West\n", 1, 4)
    if direction == 1:
        h.go_north()
    elif direction == 2:
        h.go_south()
    elif direction == 3:
        h.go_east()
    else:
        h.go_west()


main()