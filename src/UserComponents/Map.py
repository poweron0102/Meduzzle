from dataclasses import dataclass

from Components.Component import Component
from Components.TileMap import TileMap, TileMapRenderer
from Geometry import Vec2


class Map(Component):
    instance: 'Map' = None

    tile_map_texture: TileMapRenderer

    def __init__(self, tile_map: list[list[int]], solids: set[int]):
        if not Map.instance:
            Map.instance = self
        else:
            raise Exception("Map already exists")

        self.size = Vec2(len(tile_map[0]), len(tile_map))
        self.tile_map = tile_map
        self.solids = solids

    def is_solid(self, pos: Vec2[int]) -> bool:
        if pos.x < 0 or pos.y < 0 or pos.x >= self.size.x or pos.y >= self.size.y:
            return True
        return self.tile_map[pos.y][pos.x] in self.solids

    def get_word_position(self, pos: Vec2[int]) -> Vec2[float]:
        return self.tile_map_texture.get_tile_word_position(pos.x, pos.y)

    def init(self):
        self.tile_map_texture = self.GetComponent(TileMapRenderer)

    def update(self):
        pass
