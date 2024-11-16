from Components.Component import Component
from Geometry import Vec2
from UserComponents.Map import Map
from UserComponents.TiledObj import TiledObj


class Pushable(TiledObj):
    All: dict[tuple[int, int], 'Pushable'] = {}

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value: Vec2[int]):
        # if self._position in self.All:
        #    print("Error: Position already occupied")

        Pushable.All.pop(self._position.to_tuple, None)
        self._position = value
        Pushable.All[value.to_tuple] = self

    def __init__(self, position: Vec2[int]):
        self._position: Vec2[int] = position
        self.position: Vec2[int] = position

    def init(self):
        self.teleport(self.position)

    def on_destroy(self):
        if self.position.to_tuple in Pushable.All:
            Pushable.All.pop(self.position.to_tuple)

    def push(self, direction: Vec2[int]) -> bool:
        new_pos = self.position + direction
        if Map.instance.is_solid(new_pos):
            return False

        if new_pos.to_tuple in Pushable.All:
            if not Pushable.All[new_pos.to_tuple].push(direction):
                return False

        self.position = new_pos

        self.is_moving = True
        self.game.scheduler.add_generator(self.slow_move(self.position))
        return True

    def can_push(self, direction: Vec2[int]) -> bool:
        new_pos = self.position + direction
        if Map.instance.is_solid(new_pos):
            return False

        if new_pos in Pushable.All:
            return Pushable.All[new_pos].can_push(direction)

        return True
