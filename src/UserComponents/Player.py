import pygame as pg

from Components.Component import Component
from Components.Sprite import Sprite
from Geometry import Vec2
from UserComponents.Map import Map
from UserComponents.Pushable import Pushable


class Player(Component):

    sprite: Sprite

    def __init__(self, start_tile: Vec2[int]):
        self.position = start_tile
        self.is_moving = False

    def move(self, direction: Vec2[int]):
        new_pos = self.position + direction
        if Map.instance.is_solid(new_pos):
            return

        if new_pos.to_tuple in Pushable.All:
            if not Pushable.All[new_pos.to_tuple].push(direction):
                return

        print(Pushable.All)

        self.is_moving = True
        self.game.scheduler.add_generator(self.slow_move(new_pos))

    def teleport(self, target: Vec2[int]):
        self.position = target
        self.transform.position = Map.instance.get_word_position(target)

    def init(self):
        self.teleport(self.position)
        self.sprite = self.GetComponent(Sprite)

    def loop(self):
        if not self.is_moving:
            if pg.key.get_pressed()[pg.K_a]:
                self.move(Vec2(-1, 0))
                self.sprite.horizontal_flip = True
            elif pg.key.get_pressed()[pg.K_d]:
                self.move(Vec2(1, 0))
                self.sprite.horizontal_flip = False
            elif pg.key.get_pressed()[pg.K_w]:
                self.move(Vec2(0, -1))
            elif pg.key.get_pressed()[pg.K_s]:
                self.move(Vec2(0, 1))

    def slow_move(self, target: Vec2[int]):
        target_position = Map.instance.get_word_position(target)
        self.game.scheduler.add_generator(self.rotate(target.x - self.position.x))
        while self.transform.position.distance(target_position) > 1:
            direction = (target_position - self.transform.position).normalize()
            self.transform.position += direction * (self.game.delta_time * 100)
            yield
        self.position = target
        yield 0.3
        self.is_moving = False

    def rotate(self, dir: int):
        if dir == 0:
            return

        total_time = 0.5
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
