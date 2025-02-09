from EasyCells import Vec2

from UserComponents.Pushable import Pushable


class Mirror(Pushable):
    def __init__(self, start_tile: Vec2[int], map_light: dict[tuple[int, int], tuple[int, int]]):
        super().__init__(start_tile)
        self.map_light = map_light

