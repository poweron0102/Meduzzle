import pygame as pg

from Components.Camera import Drawable
from Geometry import Vec2


def panel_maker(size: Vec2[int], base_panel: pg.Surface) -> pg.Surface:
    pieces_size = (base_panel.get_width() // 3, base_panel.get_height() // 3)
    pieces = [
        [
            base_panel.subsurface(
                (x * pieces_size[0], y * pieces_size[1], pieces_size[0], pieces_size[1])
            )
            for x in range(3)
        ]
        for y in range(3)
    ]

    panel = pg.Surface(size.to_tuple, pg.SRCALPHA)

    num_of_pieces = (size.x // pieces_size[0], size.y // pieces_size[1])
    for y in range(1, num_of_pieces[1] - 1):
        for x in range(1, num_of_pieces[0] - 1):
            panel.blit(pieces[1][1], (x * pieces_size[0], y * pieces_size[1]))

    for x in range(1, num_of_pieces[0] - 1):
        panel.blit(pieces[0][1], (x * pieces_size[0], 0))
        panel.blit(pieces[2][1], (x * pieces_size[0], (num_of_pieces[1] - 1) * pieces_size[1]))

    for y in range(1, num_of_pieces[1] - 1):
        panel.blit(pieces[1][0], (0, y * pieces_size[1]))
        panel.blit(pieces[1][2], ((num_of_pieces[0] - 1) * pieces_size[0], y * pieces_size[1]))

    panel.blit(pieces[0][0], (0, 0))
    panel.blit(pieces[2][0], (0, (num_of_pieces[1] - 1) * pieces_size[1]))
    panel.blit(pieces[0][2], ((num_of_pieces[0] - 1) * pieces_size[0], 0))
    panel.blit(pieces[2][2], ((num_of_pieces[0] - 1) * pieces_size[0], (num_of_pieces[1] - 1) * pieces_size[1]))

    return panel


class Hud(Drawable):
    panel: pg.Surface

    def __init__(self, base_panel: str):
        self.base_panel = pg.image.load(f"Assets/{base_panel}")
        self.last_size = (0, 0)

    def draw(self, cam_x: float, cam_y: float, scale: float):
        self.game.screen.blit(self.panel, (0, 300))

    def loop(self):
        if self.last_size != self.game.screen.get_size():
            self.panel = panel_maker(Vec2(self.game.screen.get_width(), 300), self.base_panel)
            self.last_size = self.game.screen.get_size()
