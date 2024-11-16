from Components.Component import Component
from Geometry import Vec2
from UserComponents.Map import Map
from UserComponents.TiledObj import TiledObj


class Pushable(TiledObj):
    def __init__(self,  start_tile: Vec2[int], transparent: bool = False, transparent_after_mirror: bool = False):
        self._position: Vec2[int] = start_tile
        self.position: Vec2[int] = start_tile

        self.transparent = transparent
        self.transparent_after_mirror = transparent_after_mirror

    def init(self):
        self.teleport(self.position)

    def push(self, direction: Vec2[int]) -> bool:
        new_pos = self.position + direction
        if Map.instance.is_solid(new_pos):
            return False

        next_obj = TiledObj.AllObjs.get(new_pos.to_tuple, None)
        if next_obj is not None:
            if not type(next_obj) is Pushable:
                return False
            if not next_obj.push(direction):
                return False

        self.position = new_pos

        self.is_moving = True
        self.game.scheduler.add_generator(self.slow_move(self.position))
        return True

    def can_push(self, direction: Vec2[int]) -> bool:
        new_pos = self.position + direction
        if Map.instance.is_solid(new_pos):
            return False

        if new_pos in Pushable.AllPushable:
            return Pushable.AllPushable[new_pos].can_push(direction)

        return True
