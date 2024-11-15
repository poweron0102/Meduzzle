import math

from Geometry import Vec2

from Components.Component import Item

from Components.Animator import Animation, Animator

from Components.Camera import Camera

from Components.Sprite import Sprite

from UserComponents.Sum import Sum
from main import Game


def init(game: Game):
    game.CreateItem().AddComponent(Camera())

    sum = game.CreateItem()
    sum.AddComponent(Sum(0.008))
    sum.AddComponent(Sprite("sum.png"))

    human = game.CreateItem()
    human.AddComponent(Sprite("player24.png", (24, 24)))
    human.AddComponent(Animator({
        "stop": Animation(1000, [0]),
        "walk": Animation(0.5, [0, 1]),
    }, "walk"))

    human.transform.position = Vec2(0, -(150 + 12))

    tornado = sum.CreateChild()
    tornado.AddComponent(Sprite("tornado.png"))
    tornado.transform.position = Vec2((150 + 12), 0)
    tornado.transform.angle = math.pi / 2


def loop(game: Game):
    pass
