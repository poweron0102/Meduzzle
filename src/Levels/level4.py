from EasyCells import Game

from UserComponents.Medusa import PetrifiedMedusa
from Levels._shared import (
    SLASH_MIRROR,
    add_exit,
    add_medusa,
    add_mirror,
    add_plate,
    room,
    setup,
)

map_mat = room(walls={(1, 5), (2, 5), (3, 5), (4, 5), (6, 5), (8, 5), (9, 5), (10, 5), (11, 5)})


def init(game: Game):
    setup(game, map_mat, player_at=(10, 9), moves=90)
    add_medusa(game, (2, 7), (1, 0))
    add_medusa(game, (7, 2), (0, -1))
    add_mirror(game, (7, 9), SLASH_MIRROR, "mirror_slash.png")

    door = add_exit(game, (11, 1), "level5")
    add_plate(game, (9, 3), door, {PetrifiedMedusa})


def loop(game: Game):
    pass
