"""
Singleton Design Pattern - map of the dungeon maze
"""

class Map():
    """
    Represents the map of the dungeon maze
    """
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        """
        Create and fill the 2D map list form the file contents. Create and fill
        the 2D revealed list with all False values. The map stores the contents
        of the file and the revealed list is used to determine wheteher the contents
        of the map are displayed or not('x' if not displayed)
        """
        map_list = []
        
        with open('map-1.txt', 'r') as file:
            for line in file:
                map_list.append(line.rstrip())
                
        

    def __getitem__(self, row):
        """
        Overloaded [] operator. Returns the specified row from the map. Can be 
        used ot access a row m[r] or can be used ot access a value at a row and 
        column m[r][c]
        """
        pass

    def __len__(self):
        """
        returns the number of rows in the map list. Note: if you want to know 
        num rows, use len(m), if num of columns use len(m[r]).
        """
        map = []
        
        with open("map-1.txt", 'r') as file:
            for row in file:
                sublist = row.split()
                map.append(sublist)
                
        return len[map]


    def show_map(self, loc):
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
                # If the player coord matches, display '*'
                if row == loc[0] and column == loc[1]:
                    print('*', end=' ')
                else:
                    print(char, end=' ')
            print()

    def reveal(self, loc):
        """
        Set the value in the 2D revealed list at the specified loc to True
        """
        pass

    def remove_at_loc(self, loc):
        """
        Ovrwrites the character in the map list at the specified location with 
        an 'n'.
        """
        pass
        
