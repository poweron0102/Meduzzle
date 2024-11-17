from Components.Animator import Animator
from Geometry import Vec2
from UserComponents.TiledObj import TiledObj


class Door(TiledObj):
    def __init__(self, start_tile: Vec2[int], pass_level: str):
        self.position = start_tile
        self.is_open = False
        self.animator: Animator | None = None
        self.pass_level = pass_level

    def init(self):
        self.teleport(self.position)
        self.animator = self.GetComponent(Animator)

    def open(self):
        self.is_open = True
        self.animator.current_animation = "open"

    def close(self):
        self.is_open = False
        self.animator.current_animation = "close"
