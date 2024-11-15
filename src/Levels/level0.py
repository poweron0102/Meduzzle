import pygame as pg
from main import Game
from Components.FMODAudioManager import FMODAudioManager

fam_component: FMODAudioManager

def init(game: Game):
    global fam_component
    fam_instance = game.CreateItem()
    fam_component = fam_instance.AddComponent(FMODAudioManager(["Master.bank", "Master.strings.bank"], "music"))

def loop(game: Game):
    state = pg.mouse.get_pos()[0] / game.screen.get_width()
    bullet_time = pg.mouse.get_pos()[1] / game.screen.get_height()
    fam_component.music_instance.set_parameter_by_name("bulletTime", bullet_time)
    fam_component.music_instance.set_parameter_by_name("state", state)