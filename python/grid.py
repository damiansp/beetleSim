import numpy as np

from cell import Cell

class Grid:
    def __init__(self, dims):
        assert len(dims) == 2, 'dims must be of length 2'
        assert [type(dim) is int and dim >= 0 for dim in dims], \
            'dims must be non-negative integers'
        self.dims = dims
        self.x_dim = dims[0]
        self.y_dim = dims[1]
        self.grid = np.array([[Cell(x, y, 0) for x in range(self.x_dim)]
                              for y in range(self.y_dim)])

    def __str__(self):
        return 'Grid with dimensions %s' % self.grid.shape
