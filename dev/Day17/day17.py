import os
import itertools


class ConwayGame3d:

    active_cells: set
    x_range: list
    y_range: list
    z_range: list

    def __init__(self, initial_config: str):
        rows = initial_config.splitlines()
        self.y_range = [0, len(rows)]
        self.x_range = [0, len(rows[0])]
        self.z_range = [0, 0]
        self.active_cells = set()
        for y, row in enumerate(rows):
            for x, col in enumerate(row):
                if col == "#":
                    cell = (x, y, 0)
                    self.active_cells.add(cell)

    def evolve(self):
        self.x_range = [self.x_range[0]-1, self.x_range[1]+1]
        self.y_range = [self.y_range[0]-1, self.y_range[1]+1]
        self.z_range = [self.z_range[0]-1, self.z_range[1]+1]
        new_active_cells = self.active_cells.copy()

        cells = itertools.product(range(self.x_range[0], self.x_range[1]+1),
                                  range(self.y_range[0], self.y_range[1]+1),
                                  range(self.z_range[0], self.z_range[1]+1))
        for cell in cells:
            neighbors = self._get_neighbors(cell)
            num_active_neighbors = self._count_active(neighbors)
            if self._is_active(cell):
                if num_active_neighbors not in (2, 3):
                    new_active_cells.remove(cell)
            else:
                if num_active_neighbors == 3:
                    new_active_cells.add(cell)
        self.active_cells = new_active_cells.copy()

    def _count_active(self, cells: list) -> int:
        active = 0
        for cell in cells:
            if self._is_active(cell):
                active += 1
        return active

    def _is_active(self, cell: set):
        return cell in self.active_cells

    def _get_neighbors(self, cell) -> list:
        x, y, z = cell
        neighbors = list(itertools.product([x-1, x, x+1],
                                           [y-1, y, y+1],
                                           [z-1, z, z+1]
                                           ))
        neighbors.remove(cell)
        return neighbors

    def count_active_cells(self):
        return len(self.active_cells)

    def _fancy_print(self):
        for z in range(self.z_range[0], self.z_range[1]+1):
            print("z = " + str(z))
            for y in range(self.y_range[0], self.y_range[1]+1):
                pass


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        initial_config = file.read()

    conway = ConwayGame3d(initial_config)
    for _ in range(6):
        conway.evolve()
    print(conway.count_active_cells())
