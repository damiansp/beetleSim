# TODO:
# create_terrain()
# display_terrain()

import numpy as np

from cell import Cell


class Grid:
    def __init__(self, dims, lat_range, lon_range, elev_range):
        assert len(dims) == 2, 'dims must be of length 2'
        assert [type(dim) is int and dim >= 0 for dim in dims], \
            'dims must be non-negative integers'
        self.dims = dims
        self.x_dim = dims[0]
        self.y_dim = dims[1]
        self.lat_range = lat_range
        self.lon_range = lon_range
        self.elev_range = elev_range
        lats = self._get_linspace(self.y_dim, self.lat_range)
        lons = self._get_linspace(self.x_dim, self.lon_range)
        self.grid = np.array([[Cell(x, y, lat, lon, 0)
                               for y, lat in zip(range(self.y_dim), lats)]
                              for x, lon  in zip(range(self.x_dim), lons)])

    def _get_linspace(self, n, rng):
        return np.linspace(rng[0], rng[1], n)

    def __str__(self):
        return 'Grid with dimensions %s' % str(self.grid.shape)

    def create_terrain(self):
        min_elev, max_elev = self.elev_range
        pass

    def get_cell(self, x, y):
        return self.grid[x, y]


# Test
grid = Grid([10, 10], [-160.000, -120.000], [27.000, 42.000], [-10., 5000.])
print(grid)
cell_00 = grid.get_cell(0, 0)
cell_45 = grid.get_cell(4, 5)
cell_99 = grid.get_cell(9, 9)
print(cell_00)
print(cell_45)
print(cell_99)
