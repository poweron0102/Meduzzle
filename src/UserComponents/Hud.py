import pygame as pg

from Components.Button import panel_maker
from Components.Camera import Drawable
from Geometry import Vec2


class Hud(Drawable):
    dialog_panel: pg.Surface

    def __init__(self, base_panel: str):
        self.base_panel = pg.image.load(f"Assets/{base_panel}")
        self.last_size = (0, 0)

    def init(self):
        super().init()
        self.transform.z = -100

    def draw(self, cam_x: float, cam_y: float, scale: float):
        # # Dialog Panel
        # self.game.screen.blit(
        #     self.dialog_panel,
        #     (
        #         self.game.screen.get_width() // 2 - self.dialog_panel.get_width() // 2,
        #         self.game.screen.get_height() - self.dialog_panel.get_height() - 10
        #     )
        # )
        pass

    def loop(self):
        if self.last_size != self.game.screen.get_size():
            self.dialog_panel = panel_maker(Vec2(int(self.game.screen.get_width() * 0.8), 150), self.base_panel)
            self.last_size = self.game.screen.get_size()
