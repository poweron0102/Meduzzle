from Components.Component import Component
from Geometry import Vec2
from UserComponents.Map import Map


class Pushable(Component):
    All: dict[tuple[int, int], 'Pushable'] = {}

    _position: Vec2[int]

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
        self.game.scheduler.add_generator(self.slow_move(value))

    def __init__(self, position: Vec2[int]):
        self._position = position

    def init(self):
        self.teleport(self._position)

    def on_destroy(self):
        Pushable.All.pop(self._position.to_tuple)

    def push(self, direction: Vec2[int]) -> bool:
        new_pos = self._position + direction
        if Map.instance.is_solid(new_pos):
            return False

        if new_pos.to_tuple in Pushable.All:
            if not Pushable.All[new_pos.to_tuple].push(direction):
                return False

        self.position = new_pos
        return True

    def can_push(self, direction: Vec2[int]) -> bool:
        new_pos = self._position + direction
        if Map.instance.is_solid(new_pos):
            return False

        if new_pos in Pushable.All:
            return Pushable.All[new_pos].can_push(direction)

        return True

    def teleport(self, target: Vec2[int]):
        if self._position.to_tuple in Pushable.All:
            Pushable.All.pop(self._position.to_tuple)

        Pushable.All[target.to_tuple] = self
        self._position = target
        self.transform.position = Map.instance.get_word_position(target)

    def slow_move(self, target: Vec2[int]):
        target_position = Map.instance.get_word_position(target)
        while self.transform.position.distance(target_position) > 1:
            direction = (target_position - self.transform.position).normalize()
            self.transform.position += direction * (self.game.delta_time * 100)
            yield
        self.transform.position = target_position
