from dev.Day17.day17 import ConwayGame3d, ConwayGame4d


def test1():
    initial_state = """.#.
..#
###"""
    conway = ConwayGame3d(initial_state)
    for _ in range(6):
        conway.evolve()

    assert 112 == conway.count_active_cells()


def test2():
    initial_state = """.#.
..#
###"""
    conway = ConwayGame4d(initial_state)
    for _ in range(6):
        conway.evolve()

    assert 848 == conway.count_active_cells()
