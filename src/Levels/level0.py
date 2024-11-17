from Components.Camera import Camera
from Components.FMODAudioManager import FMODAudioManager
from Components.Sprite import Sprite
from Components.TileMap import TileMapRenderer, TileMap
from Geometry import Vec2
from UserComponents.Hud import Hud
from UserComponents.Map import Map
from UserComponents.Medusa import Medusa
from UserComponents.Mirror import Mirror
from UserComponents.Player import Player
from UserComponents.Pushable import Pushable
from main import Game

fam_component: FMODAudioManager

map_mat = [
    [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
    [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
    [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
    [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
    [14, 14, 14, 14, 14, 14, 18, 14, 14, 14, 14, 14, 14],
    [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
    [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
    [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
    [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14],
]


def init(game: Game):
    # global fam_component
    # fam_component = game.CreateItem().AddComponent(
    #     FMODAudioManager(["Master.bank", "Master.strings.bank"], "music")
    # )
    game.CreateItem().AddComponent(Camera((500, 600)))

    map_comp = game.CreateItem()
    map_comp.AddComponent(TileMap(map_mat))
    map_comp.AddComponent(TileMapRenderer("tilemap.png", 16))
    map_comp.AddComponent(Map(map_mat, {18}))

    player = game.CreateItem()
    player.AddComponent(Sprite("player.png"))
    player.AddComponent(Player(Vec2(2, 0), Vec2(1, 0), 99))

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
    mirror0.AddComponent(Mirror(Vec2(7, 5), {
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

    # dead = game.CreateItem()
    # #dead = player.CreateChild()
    # dead.AddComponent(Button(
    #     Vec2(80, 80),
    #     "You died",
    #     base_panel=pg.image.load("Assets/UI/Panel/panel-018.png"),
    #     hover_panel=pg.image.load("Assets/UI/Border/panel-border-000.png"),
    #     on_click=lambda: game.new_game(game.current_level),
    #     screen_space=True
    # ))
    # dead.transform.scale = 0.2


def loop(game: Game):
    pass
