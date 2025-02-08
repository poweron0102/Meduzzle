from Components.Animator import Animator, Animation
from Components.Camera import Camera
from Components.Component import Item
from Components.FMODAudioManager import FMODAudioManager
from Components.Sprite import Sprite
from Components.TileMap import TileMapRenderer, TileMap
from Geometry import Vec2
from UserComponents.Door import Door
from UserComponents.Hud import Hud
from UserComponents.Map import Map
from UserComponents.Medusa import Medusa
from UserComponents.Mirror import Mirror
from UserComponents.Player import Player
from UserComponents.Pushable import Pushable
from main import Game

fam_component: FMODAudioManager

map_mat = [
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3],
    [13, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15],
    [13, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 15],
    [13, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 15],
    [13, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 15],
    [13, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 15],
    [13, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 15],
    [13, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 15],
    [13, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 15],
    [13, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 15],
    [25, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26, 27],
]

door: Item


def init(game: Game):
    global door
    # global fam_component
    # fam_component = game.CreateItem().AddComponent(
    #     FMODAudioManager(["Master.bank", "Master.strings.bank"], "music")
    # )
    game.CreateItem().AddComponent(Camera((500, 600)))

    map_comp = game.CreateItem()
    map_comp.AddComponent(TileMap(map_mat))
    map_comp.AddComponent(TileMapRenderer("tilemap.png", 16))
    map_comp.AddComponent(Map(map_mat, {2, 3, 26, 15, 1, 3, 25, 27, 14, 13}))

    player = game.CreateItem()
    player.AddComponent(Sprite("player.png"))
    player.AddComponent(Player(Vec2(2, 8), Vec2(1, 0), 99))

    obj0 = game.CreateItem()
    obj0.AddComponent(Sprite("crate.png"))
    obj0.AddComponent(Pushable(Vec2(3, 6)))

    obj1 = game.CreateItem()
    obj1.AddComponent(Sprite("crate.png"))
    obj1.AddComponent(Pushable(Vec2(6, 6)))

    hud = game.CreateItem()
    hud.AddComponent(Hud("UI/Panel/panel-018.png"))

    medusa0 = game.CreateItem()
    medusa0.AddComponent(Sprite("medusa.png"))
    medusa0.AddComponent(Medusa(Vec2(3, 3), Vec2(1, 0)))

    mirror0 = game.CreateItem()
    mirror0.AddComponent(Mirror(Vec2(11, 5), {
        (0, 1): (1, 0),
        (1, 0): (0, 1),
        (0, -1): (-1, 0),
        (-1, 0): (0, -1),
    }))
    mirror0.AddComponent(Sprite("mirror1.png"))

    mirror1 = game.CreateItem()
    mirror1.AddComponent(Mirror(Vec2(9, 5), {
        (0, 1): (0, -1),
        (1, 0): (-1, 0),
        (0, -1): (0, 1),
        (-1, 0): (1, 0),
    }))
    mirror1.AddComponent(Sprite("mirror2.png"))

    door = game.CreateItem()
    door.AddComponent(Sprite("door.png", (16, 16)))
    door.AddComponent(Animator(
        {
            "opened": Animation(100, [3]),
            "closed": Animation(100, [0]),
            "open": Animation(0.2, [0, 1, 2, 3], "opened"),
            "close": Animation(0.2, [3, 2, 1, 0], "closed"),
        },
        "closed"
    ))
    door.AddComponent(Door(Vec2(10, 1), "level1"))


def loop(game: Game):
    pass
