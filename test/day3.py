from dev.Day3 import day3
import numpy as np


def test_example():
    grove_map = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".splitlines()

    assert 7 == day3.count_trees(grove_map, (3, 1))


def test_example2():

    grove_map = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".splitlines()

    directions = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees_in_directions = day3.trees_in_directions(grove_map, directions)
    assert 336 == np.prod(trees_in_directions)
