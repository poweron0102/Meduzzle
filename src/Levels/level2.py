from EasyCells import Game

from UserComponents.Medusa import PetrifiedMedusa
from Levels._shared import add_exit, add_medusa, add_plate, room, setup


map_mat = room(walls={(7, 5), (8, 5), (9, 5), (10, 5)})


def init(game: Game):
    setup(game, map_mat, player_at=(1, 8), moves=60)
    add_medusa(game, (3, 3), (1, 0))
    add_medusa(game, (8, 3), (0, 1))

    door = add_exit(game, (11, 1), "level3")
    add_plate(game, (5, 6), door, {PetrifiedMedusa})


def loop(game: Game):
    pass
