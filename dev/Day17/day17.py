import os
import itertools
from abc import ABC, abstractmethod
from collections.abc import Iterator


class ConwayGame_N_dim(ABC):
    """
        Basics of N dimensional Conway Game of Life
    """
    active_cells: set

    @abstractmethod
    def _get_cells_to_check(self) -> Iterator:
        """Returns those cells that will be checked in ::evolve step"""
        pass

    @abstractmethod
    def _get_neighbors(self, cell) -> Iterator:
        """Returns a list with the current neighbours of @cell"""
        pass

    def count_active_cells(self):
        return len(self.active_cells)

    def evolve(self):
        new_active_cells = self.active_cells.copy()

        cells = self._get_cells_to_check()
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

    def _is_active(self, cell: set):
        return cell in self.active_cells

    def _count_active(self, cells: list) -> int:
        return sum(self._is_active(cell) for cell in cells)


class ConwayGame3d(ConwayGame_N_dim):

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

    def _get_cells_to_check(self) -> Iterator:
        self.x_range = [self.x_range[0]-1, self.x_range[1]+1]
        self.y_range = [self.y_range[0]-1, self.y_range[1]+1]
        self.z_range = [self.z_range[0]-1, self.z_range[1]+1]

        return itertools.product(
                          range(self.x_range[0], self.x_range[1]+1),
                          range(self.y_range[0], self.y_range[1]+1),
                          range(self.z_range[0], self.z_range[1]+1))

    def _get_neighbors(self, cell) -> list:
        x, y, z = cell
        neighbors = list(itertools.product([x-1, x, x+1],
                                           [y-1, y, y+1],
                                           [z-1, z, z+1]
                                           ))
        neighbors.remove(cell)
        return neighbors


class ConwayGame4d(ConwayGame_N_dim):

    x_range: list
    y_range: list
    z_range: list
    w_range: list

    def __init__(self, initial_config: str):
        rows = initial_config.splitlines()
        self.y_range = [0, len(rows)]
        self.x_range = [0, len(rows[0])]
        self.z_range = [0, 0]
        self.w_range = [0, 0]

        self.active_cells = set()
        for y, row in enumerate(rows):
            for x, col in enumerate(row):
                if col == "#":
                    cell = (x, y, 0, 0)
                    self.active_cells.add(cell)

    def _get_cells_to_check(self) -> Iterator:
        active_cell_t = list(map(list, zip(*self.active_cells)))

        self.x_range = [min(active_cell_t[0]), max(active_cell_t[0])]
        self.y_range = [min(active_cell_t[1]), max(active_cell_t[1])]
        self.z_range = [min(active_cell_t[2]), max(active_cell_t[2])]
        self.w_range = [min(active_cell_t[3]), max(active_cell_t[3])]

        return itertools.product(
                          range(self.x_range[0]-1, self.x_range[1]+2),
                          range(self.y_range[0]-1, self.y_range[1]+2),
                          range(self.z_range[0]-1, self.z_range[1]+2),
                          range(self.w_range[0]-1, self.w_range[1]+2))

    def _get_neighbors(self, cell) -> list:
        x, y, z, w = cell
        neighbors = list(itertools.product([x-1, x, x+1],
                                           [y-1, y, y+1],
                                           [z-1, z, z+1],
                                           [w-1, w, w+1]
                                           ))
        neighbors.remove(cell)
        return neighbors


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        initial_config = file.read()

    conway = ConwayGame3d(initial_config)
    for _ in range(6):
        conway.evolve()
    print(conway.count_active_cells())

    conway = ConwayGame4d(initial_config)
    for _ in range(6):
        conway.evolve()
    print(conway.count_active_cells())
