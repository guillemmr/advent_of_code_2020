from dev.Day17.day17 import ConwayGame3d


def test1():
    initial_state = """.#.
..#
###"""
    conway = ConwayGame3d(initial_state)
    for _ in range(6):
        conway.evolve()

    assert 112 == conway.count_active_cells()
