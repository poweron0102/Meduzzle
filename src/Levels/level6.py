from EasyCells import Game

from UserComponents.Medusa import PetrifiedMedusa
from Levels._shared import (
    BACKSLASH_MIRROR,
    add_exit,
    add_medusa,
    add_mirror,
    add_plate,
    room,
    setup,
)

map_mat = room(walls={(1, 4), (2, 4), (4, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4)})


def init(game: Game):
    setup(game, map_mat, player_at=(10, 9), moves=110)

    add_medusa(game, (2, 2), (1, 0))
    add_medusa(game, (10, 6), (0, 1))
    add_mirror(game, (5, 1), BACKSLASH_MIRROR, "mirror_backslash.png")
    add_mirror(game, (3, 6), BACKSLASH_MIRROR, "mirror_backslash.png")

    door = add_exit(game, (11, 1), "level0")
    add_plate(game, (9, 8), door, {PetrifiedMedusa})


def loop(game: Game):
    pass
