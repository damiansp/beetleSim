class Cell:
    def __init__(self, x, y, alt):
        assert x >= 0 and y >= 0, 'Cell coordinates must be positive integers'
        self.x = int(x)
        self.y = int(y)
        self.alt = alt

    def __str__(self):
        return 'Cell at (%d, %d), alt: %.2f' % (self.x, self.y, self.alt)

    def init_tree_population(self, Tree):
        self.Tree = Tree

    def init_beetle_population(self, Beetle):
        


# Test
#c1 = Cell(0, 0, 33.78897)
#print(c1)
