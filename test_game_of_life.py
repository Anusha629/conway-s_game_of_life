import game_of_life

def test_get_empty_grid():
    grid = game_of_life.get_empty_grid(3, 3)
    expected_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert grid == expected_grid

    grid = game_of_life.get_empty_grid(0, 0)
    expected_grid = []
    assert grid == expected_grid