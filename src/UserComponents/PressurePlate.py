from typing import Type

from Components.Component import Component
from Geometry import Vec2
from UserComponents.Map import Map
from UserComponents.TiledObj import TiledObj


class PressurePlate(Component):
    def __init__(self, start_tile: Vec2[int], active_with: set[Type[TiledObj]], on_active: callable,
                 on_deactivate: callable):
        self.position = start_tile
        self.active_with = active_with
        self.on_active = on_active
        self.on_deactivate = on_deactivate

        self.is_active = False

    def init(self):
        self.teleport(self.position)

    def loop(self):
        if not self.is_active and (obj := TiledObj.AllObjs.get(self.position.to_tuple, None)):
            for obj_type in self.active_with:
                if isinstance(obj, obj_type):
                    self.is_active = True
                    self.on_active()
                    return
        elif self.is_active and not TiledObj.AllObjs.get(self.position.to_tuple, None):
            self.is_active = False
            self.on_deactivate()
        elif self.is_active and (obj := TiledObj.AllObjs.get(self.position.to_tuple, None)):
            for obj_type in self.active_with:
                if isinstance(obj, obj_type):
                    return
            self.is_active = False
            self.on_deactivate()

    def teleport(self, target: Vec2[int]):
        self.position = target
        self.transform.position = Map.instance.get_word_position(target)
