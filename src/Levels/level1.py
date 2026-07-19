from EasyCells import Game

from UserComponents.Pushable import Pushable
from Levels._shared import add_crate, add_exit, add_medusa, add_plate, room, setup


map_mat = room(
    walls={
        (1, 4), (2, 4), (3, 4), (4, 4),
        (5, 4), (6, 4), (7, 4), (8, 4),
    },
)


def init(game: Game):
    setup(game, map_mat, player_at=(1, 8), moves=60)
    add_crate(game, (3, 6))
    add_medusa(game, (2, 2), (0, 1))

    door = add_exit(game, (11, 1), "level2")
    add_plate(game, (9, 2), door, {Pushable})


def loop(game: Game):
    pass
