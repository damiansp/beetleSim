# TODO:
# populate_trees
import matplotlib.pyplot as plt
import numpy as np
#from maplotlib import image

from cell import Cell


def get_dist(p1, p2):
    return np.sqrt(((p1 - p2) ** 2).sum())


class Grid:
    def __init__(self, dims, lat_range, lon_range, elev_range):
        assert len(dims) == 2, 'dims must be of length 2'
        assert [type(dim) is int and dim >= 0 for dim in dims], \
            'dims must be non-negative integers'
        self.dims = dims
        self.x_dim = dims[0]
        self.y_dim = dims[1]
        self.n = self.x_dim * self.y_dim
        self.lat_range = lat_range
        self.lon_range = lon_range
        self.elev_range = elev_range
        lats = self._get_linspace(self.y_dim, self.lat_range)
        lons = self._get_linspace(self.x_dim, self.lon_range)
        self.grid = np.array([
            [Cell(x, y, lat, lon, 0) for y, lat in zip(range(self.y_dim), lats)]
            for x, lon  in zip(range(self.x_dim), lons)])

    def _get_linspace(self, n, rng):
        return np.linspace(rng[0], rng[1], n)

    def __str__(self):
        return 'Grid with dimensions %s' % str(self.grid.shape)

    def create_terrain(self, ruggedness=0.02, falloff=1.5):
        min_elev, max_elev = self.elev_range
        n_peaks = int(np.round(self.n * ruggedness))
        heights = np.random.uniform(0.5, 1, size=n_peaks)
        peak_locations = [
            np.array([np.random.randint(0, self.x_dim),
                      np.random.randint(0, self.y_dim)])
            for peak in range(n_peaks)]
        dists = np.array([[[get_dist(peak, [x, y])for x in range(self.x_dim)]
                           for y in range(self.y_dim)]
                          for peak in peak_locations])
        weights = 1 / (dists + 1) ** falloff
        for i, h in enumerate(heights):
            weights[i] *= h
        elevation = np.sum(weights, axis=0) / n_peaks
        elevation /= elevation.max().max()
        for x in range(self.x_dim):
            for y in range(self.y_dim):
                self.grid[x, y].elevation = elevation[x, y]

    def populate_trees(self):
        pass
    
    def plot_elevation(self):
        m = [[self.grid[x, y].elevation for x in range(self.x_dim)]
             for y in range(self.y_dim)]
        plt.imshow(m)
        plt.colorbar()
        plt.title(f'Elevation / {int(self.elev_range[1])}')
        plt.show()
             
    def get_cell(self, x, y):
        return self.grid[x, y]


# Test
grid = Grid([50, 50], [-160.000, -120.000], [27.000, 42.000], [-10., 5000.])
print(grid)
grid.create_terrain()
grid.plot_elevation()
