from Components.Component import Component
from Geometry import Vec2
from UserComponents.Map import Map
from UserComponents.TiledObj import TiledObj


class Pushable(TiledObj):
    AllPushable: dict[tuple[int, int], 'Pushable'] = {}

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value: Vec2[int]):
        # if self._position in self.AllPushable:
        #    print("Error: Position already occupied")

        Pushable.AllPushable.pop(self._position.to_tuple, None)
        self._position = value
        Pushable.AllPushable[value.to_tuple] = self

    def __init__(self,  start_tile: Vec2[int]):
        self._position: Vec2[int] = start_tile
        self.position: Vec2[int] = start_tile

    def init(self):
        self.teleport(self.position)

    def on_destroy(self):
        if self.position.to_tuple in Pushable.AllPushable:
            Pushable.AllPushable.pop(self.position.to_tuple)

    def push(self, direction: Vec2[int]) -> bool:
        new_pos = self.position + direction
        if Map.instance.is_solid(new_pos):
            return False

        if new_pos.to_tuple in Pushable.AllPushable:
            if not Pushable.AllPushable[new_pos.to_tuple].push(direction):
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
