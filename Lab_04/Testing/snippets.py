def read_map():
    """Read the contents of map.txt and store the contents in a 2D list,
    then return the filled list"""
    
    map = []

    # map.txt has char delimited a ' '
    with open("map.txt", 'r') as file:
        for row in file:
            sublist = row.split()
            map.append(sublist)

    return map