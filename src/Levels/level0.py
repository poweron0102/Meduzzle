import pygame as pg

from Components.Camera import Camera
from Components.Sprite import Sprite
from Components.TileMap import TileMapRenderer, TileMap
from Geometry import Vec2
from UserComponents.Map import Map
from UserComponents.Player import Player
from UserComponents.Pushable import Pushable
from main import Game
from Components.FMODAudioManager import FMODAudioManager

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
    player.AddComponent(Player(Vec2(2, 0)))

    obj0 = game.CreateItem()
    obj0.AddComponent(Sprite("crate.png"))
    obj0.AddComponent(Pushable(Vec2(3, 6)))

    obj1 = game.CreateItem()
    obj1.AddComponent(Sprite("crate.png"))
    obj1.AddComponent(Pushable(Vec2(6, 6)))


def loop(game: Game):
    pass
    # state = pg.mouse.get_pos()[0] / game.screen.get_width()
    # bullet_time = pg.mouse.get_pos()[1] / game.screen.get_height()
    # fam_component.music_instance.set_parameter_by_name("bulletTime", bullet_time)
    # fam_component.music_instance.set_parameter_by_name("state", state)

    #  player moves
