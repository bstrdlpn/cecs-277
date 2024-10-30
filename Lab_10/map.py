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
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
        Create and fill the 2D map list form the file contents. Create and fill
        the 2D revealed list with all False values. The map stores the contents
        of the file and the revealed list is used to determine wheteher the contents
        of the map are displayed or not('x' if not displayed)
        """
        with open('map-1.txt', 'r') as file:
            self._map = [list(line.rstrip()) for line in file]
        
        self._revealed = [[False for char in row] for row in self._map]

    def __getitem__(self, row):
        """
        Overloaded [] operator. Returns the specified row from the map. Can be 
        used ot access a row m[r] or can be used ot access a value at a row and 
        column m[r][c]
        """
        if isinstance(row, int):
            return self._map[row]
        elif isinstance(row, tuple) and len(row) == 2:
            r, c = row
            return self._map[r][c]
        else:
            raise IndexError("Invalid index, must be a row or a tuple of two integers.")

    def __len__(self):
        """
        returns the number of rows in the map list. Note: if you want to know 
        num rows, use len(m), if num of columns use len(m[r]).
        """
        # if the map list is empty
        if not self._map:
            return 0
        else:
            return len(self._map)

    def show_map(self, loc):
        """
        Return the map as a string in the format of a 5x5 matrix of chars where
        each revealed = chars from map. Unrevealed = 'x', hero = '*'

        :param loc: tuple; location of hero char
        """
        revealed_map = []
        
        for i in range(5):
            row = []
            for j in range(5):
                # where hero char is, append *
                if (i, j) == loc:
                    row.append('*')
                # if True, append char from map
                elif self._revealed[i][j]:
                    row.append(self._map[i][j])
                # False, append 'x'
                else:
                    row.append('x')
            revealed_map.append(' '.join(row))
        
        return '\n'.join(revealed_map)

    def reveal(self, loc):
        """
        Set the value in the 2D revealed list at the specified loc to True.

        :param loc: tuple; index of the specified bool
        """
        r, c = loc
        self._revealed[r][c] = True

    def remove_at_loc(self, loc):
        """
        Overwrite the char in the map list at the specified location with 'n'.

        :param loc: tuple; index of the specified char
        """
        r,c = loc
        self._map[r][c] = 'n'
        
