class Cell:
    def __init__(self, x, y, lat, lon, alt):
        '''x and y are simply int indices for the matrix'''
        assert x >= 0 and y >= 0, 'Cell coordinates must be positive integers'
        self.x = int(x)
        self.y = int(y)
        self.lat = lat
        self.lon = lon
        self.alt = alt

    def __str__(self):
        return ('Cell at (%d, %d):\n  lat: %.4f\n  lon: %.4f\n  alt: %.2f'
                % (self.x, self.y, self.lat, self.lon, self.alt))

    def init_tree_population(self, Tree):
        self.Tree = Tree

    def init_beetle_population(self, Beetle):
        self.Beetle = Beetle


# Test
c1 = Cell(0, 0, 33.78897, -127.2242, 57.9)
print(c1)
