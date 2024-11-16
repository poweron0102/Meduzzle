from typing import Callable

from Components.Component import Component
from Geometry import Vec2
from UserComponents.Map import Map


class TiledObj(Component):
    AllObjs: dict[tuple[int, int], 'TiledObj'] = {}

    _position: Vec2[int] = Vec2(0, 0)
    position: Vec2[int]

    is_moving: bool

    transparent: bool = False
    transparent_after_mirror: bool = False

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value: Vec2[int]):
        # if self._position in self.AllPushable:
        #    print("Error: Position already occupied")

        TiledObj.AllObjs.pop(self._position.to_tuple, None)
        self._position = value
        TiledObj.AllObjs[value.to_tuple] = self

    def on_destroy(self):
        if self.position.to_tuple in TiledObj.AllObjs:
            TiledObj.AllObjs.pop(self.position.to_tuple)

    def teleport(self, target: Vec2[int]):
        self.position = target
        self.transform.position = Map.instance.get_word_position(target)

    def slow_move(self, target: Vec2[int]):
        target_position = Map.instance.get_word_position(target)
        self.game.scheduler.add_generator(self.rotate(target.x - self.position.x))
        while self.transform.position.distance(target_position) > 1:
            direction = (target_position - self.transform.position).normalize()
            self.transform.position += direction * (self.game.delta_time * 100)
            yield
        self.position = target
        yield 0.1
        self.is_moving = False

    def rotate(self, dir: int):
        if dir == 0:
            return

        total_time = 0.3
        start_time = self.game.run_time
        while self.game.run_time - start_time < 0.4 * total_time:
            self.transform.angle_deg += dir * -80 * self.game.delta_time
            yield
        while self.game.run_time - start_time < 0.8 * total_time:
            self.transform.angle_deg += dir * 120 * self.game.delta_time
            yield
        while self.game.run_time - start_time < total_time:
            self.transform.angle_deg += dir * -80 * self.game.delta_time
            yield

        self.transform.angle = 0
