from EasyCells import Game, Vec2
from EasyCells.Components import Animation, Animator, Camera, Sprite, TileMap
from EasyCells.Components.TileMap import TileMapRenderer

from UserComponents.Door import Door
from UserComponents.Hud import Hud
from UserComponents.Map import Map
from UserComponents.Medusa import Medusa, PetrifiedMedusa
from UserComponents.Mirror import Mirror
from UserComponents.Player import Player
from UserComponents.PressurePlate import PressurePlate
from UserComponents.Pushable import Pushable


FLOOR = 14
WALL = 18

BACKSLASH_MIRROR = {
    (1, 0): (0, 1),
    (0, 1): (1, 0),
    (-1, 0): (0, -1),
    (0, -1): (-1, 0),
}

SLASH_MIRROR = {
    (1, 0): (0, -1),
    (0, -1): (1, 0),
    (-1, 0): (0, 1),
    (0, 1): (-1, 0),
}


def room(width: int = 13, height: int = 11, walls=()):
    tiles = [[FLOOR for _ in range(width)] for _ in range(height)]
    for x, y in walls:
        tiles[y][x] = WALL
    return tiles


def setup(game: Game, tiles: list[list[int]], player_at: tuple[int, int], moves: int):
    game.CreateItem().AddComponent(Camera((300, 225)))

    map_item = game.CreateItem()
    map_item.AddComponent(TileMap(tiles))
    map_item.AddComponent(TileMapRenderer("tilemap.png", 16))
    map_item.AddComponent(Map(tiles, {WALL}))
    map_item.transform.z = 100

    player = game.CreateItem()
    player.AddComponent(Sprite("player.png"))
    player.AddComponent(Player(Vec2(*player_at), Vec2(1, 0), moves))

    game.CreateItem().AddComponent(Hud("UI/Panel/panel-018.png"))


def add_crate(game: Game, at: tuple[int, int]):
    item = game.CreateItem()
    item.AddComponent(Sprite("crate.png"))
    return item.AddComponent(Pushable(Vec2(*at)))


def add_statue(game: Game, at: tuple[int, int]):
    item = game.CreateItem()
    item.AddComponent(Sprite("medusa_o.png"))
    return item.AddComponent(PetrifiedMedusa(Vec2(*at)))


def add_medusa(game: Game, at: tuple[int, int], looking: tuple[int, int]):
    item = game.CreateItem()
    item.AddComponent(Sprite("medusa.png"))
    return item.AddComponent(Medusa(Vec2(*at), Vec2(*looking)))


def add_mirror(game: Game, at: tuple[int, int], light_map, sprite: str):
    item = game.CreateItem()
    item.AddComponent(Sprite(sprite))
    return item.AddComponent(Mirror(Vec2(*at), light_map))


def add_exit(game: Game, at: tuple[int, int], next_level: str):
    item = game.CreateItem()
    item.AddComponent(Sprite("door.png", (16, 16)))
    item.AddComponent(Animator(
        {
            "opened": Animation(100, [3]),
            "closed": Animation(100, [0]),
            "open": Animation(0.2, [0, 1, 2, 3], "opened"),
            "close": Animation(0.2, [3, 2, 1, 0], "closed"),
        },
        "closed",
    ))
    return item.AddComponent(Door(Vec2(*at), next_level))


def add_plate(game: Game, at: tuple[int, int], door: Door, active_with):
    item = game.CreateItem()
    item.AddComponent(Sprite("pressure_plate.png"))
    item.AddComponent(
        PressurePlate(Vec2(*at), set(active_with), door.open, door.close)
    )
    item.transform.z = 5
