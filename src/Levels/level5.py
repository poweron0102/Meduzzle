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

map_mat = room(walls={(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (6, 8), (7, 8), (8, 8)})


def init(game: Game):
    setup(game, map_mat, player_at=(10, 9), moves=95)
    add_medusa(game, (2, 2), (1, 0))
    add_medusa(game, (9, 7), (0, 1))
    add_mirror(game, (6, 1), BACKSLASH_MIRROR, "mirror_backslash.png")
    add_mirror(game, (4, 7), BACKSLASH_MIRROR, "mirror_backslash.png")

    door = add_exit(game, (11, 1), "level6")
    add_plate(game, (3, 5), door, {PetrifiedMedusa})


def loop(game: Game):
    pass
