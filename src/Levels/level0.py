import pygame as pg

from Components.Camera import Camera
from Components.Component import Item
from Components.Sprite import Sprite
from main import Game
from Components.FMODAudioManager import FMODAudioManager

fam_component: FMODAudioManager

player: Item


def init(game: Game):
    global fam_component, player
    fam_instance = game.CreateItem()
    fam_component = fam_instance.AddComponent(FMODAudioManager(["Master.bank", "Master.strings.bank"], "music"))

    game.CreateItem().AddComponent(Camera())

    player = game.CreateItem()
    player.AddComponent(Sprite("player.png"))


def loop(game: Game):
    state = pg.mouse.get_pos()[0] / game.screen.get_width()
    bullet_time = pg.mouse.get_pos()[1] / game.screen.get_height()
    fam_component.music_instance.set_parameter_by_name("bulletTime", bullet_time)
    fam_component.music_instance.set_parameter_by_name("state", state)

    #  player moves
    if pg.key.get_pressed()[pg.K_a]:
        player.transform.x -= 100 * game.delta_time
    if pg.key.get_pressed()[pg.K_d]:
        player.transform.x += 100 * game.delta_time
    if pg.key.get_pressed()[pg.K_w]:
        player.transform.y -= 100 * game.delta_time
    if pg.key.get_pressed()[pg.K_s]:
        player.transform.y += 100 * game.delta_time
