from Geometry import Vec2
from UserComponents.Map import Map
from UserComponents.TiledObj import TiledObj


class Medusa(TiledObj):

    def __init__(self, start_tile: Vec2[int], looking: Vec2[int]):
        self._position: Vec2[int] = start_tile
        self.position = start_tile
        self.is_moving = False

    def init(self):
        self.teleport(self.position)

    def loop(self):
        pass

    @staticmethod
    def is_looking_to_medusa(pos: Vec2[int], looking: Vec2[int], mirror: bool = False) -> bool:
        new_pos = pos + looking

        if Map.instance.is_solid(new_pos):
            return False

        next_obj = TiledObj.AllObjs.get(new_pos.to_tuple, None)
        if next_obj is not None:
            if type(next_obj) is Medusa:
                return True
            if mirror:
                if not next_obj.transparent_after_mirror:
                    return False
            else:
                if not next_obj.transparent:
                    return False

        return Medusa.is_looking_to_medusa(new_pos, looking)
