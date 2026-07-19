from EasyCells import Game

from UserComponents.Pushable import Pushable
from Levels._shared import add_crate, add_exit, add_plate, room, setup


map_mat = room(
    height=7,
    walls={(9, 0), (9, 1), (9, 2), (9, 3)},
)


def init(game: Game):
    setup(game, map_mat, player_at=(1, 5), moves=35)
    add_crate(game, (3, 4))

    door = add_exit(game, (11, 1), "level1")
    add_plate(game, (8, 4), door, {Pushable})


def loop(game: Game):
    pass
