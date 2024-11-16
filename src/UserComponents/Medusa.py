from Geometry import Vec2
from UserComponents.Map import Map
from UserComponents.TiledObj import TiledObj


class Medusa(TiledObj):
    AllMedusa: dict[tuple[int, int], 'Medusa'] = {}

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value: Vec2[int]):
        # if self._position in self.AllPushable:
        #    print("Error: Position already occupied")

        Medusa.AllMedusa.pop(self._position.to_tuple, None)
        self._position = value
        Medusa.AllMedusa[value.to_tuple] = self

    def __init__(self, start_tile: Vec2[int], looking: Vec2[int]):
        self._position: Vec2[int] = start_tile
        self.position = start_tile
        self.is_moving = False

    def init(self):
        self.teleport(self.position)

    def loop(self):
        pass

    @staticmethod
    def is_looking_to_medusa(pos: Vec2[int], looking: Vec2[int]) -> bool:
        new_pos = pos + looking
        if new_pos.to_tuple in Medusa.AllMedusa:
            return True

        if Map.instance.is_solid(new_pos):
            return False

        return Medusa.is_looking_to_medusa(new_pos, looking)
