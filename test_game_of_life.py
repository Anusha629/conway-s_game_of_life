import game_of_life

def test_get_empty_grid():
    grid = game_of_life.get_empty_grid(3, 3)
    expected_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert grid == expected_grid

    grid = game_of_life.get_empty_grid(0, 0)
    expected_grid = []
    assert grid == expected_grid

def test_update_grid_no_changes():
    game_of_life.HEIGHT = 3
    game_of_life.WIDTH = 3
    grid = game_of_life.get_empty_grid(game_of_life.WIDTH, game_of_life.HEIGHT)
    expected_grid = game_of_life.get_empty_grid(game_of_life.WIDTH, game_of_life.HEIGHT)
    new_grid = game_of_life.update_grid(grid)
    assert new_grid == expected_grid