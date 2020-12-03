import os
import numpy as np


def get_coordinate(grove_map: list, x: int, y: int) -> bool:
    length = len(grove_map[0])
    return grove_map[y][x % length]


def count_trees(grove_map: list, direction: tuple) -> int:
    """ # of trees that will be encountered going each direction step."""
    coord = [0, 0]
    trees_in_path = 0
    end_of_path = False

    while end_of_path is not True:
        if get_coordinate(grove_map, coord[0], coord[1]) == "#":
            trees_in_path = trees_in_path + 1

        coord[0] = coord[0] + direction[0]
        coord[1] = coord[1] + direction[1]

        if len(grove_map) <= coord[1]:
            end_of_path = True

    return trees_in_path


def trees_in_directions(grove_map: list, directions: list) -> list:
    """ returns a list with the number of collision trees for each direction"""
    number_of_trees = []
    for direction in directions:
        number_of_trees.append(count_trees(grove_map, direction))
    return number_of_trees


if __name__ == "__main__":

    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        grove_map = file.read().splitlines()

    directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees_in_directions = trees_in_directions(grove_map, directions)
    print(np.prod(trees_in_directions))
