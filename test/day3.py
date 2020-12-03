from dev.Day3 import day3


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
