import pygame as pg

from Components.Component import Component
from Components.Sprite import Sprite
from Geometry import Vec2
from UserComponents.Map import Map
from UserComponents.Pushable import Pushable
from UserComponents.TiledObj import TiledObj


class Player(TiledObj):
    sprite: Sprite

    def __init__(self, start_tile: Vec2[int], looking: Vec2[int], moves: int):
        self.position = start_tile
        self.is_moving = False
        self.moves = moves
        self.looking = looking

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

        if self.moves == 0:
            self.game.new_game(self.game.current_level)

    def move(self, direction: Vec2[int]):
        self.looking = direction
        new_pos = self.position + direction
        if Map.instance.is_solid(new_pos):
            return

        if new_pos.to_tuple in Pushable.AllPushable:
            if not Pushable.AllPushable[new_pos.to_tuple].push(direction):
                return

        self.moves -= 1
        self.is_moving = True
        self.game.scheduler.add_generator(self.slow_move(new_pos))
