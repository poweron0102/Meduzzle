from Geometry import Vec2
from UserComponents.Map import Map
from UserComponents.Mirror import Mirror
from UserComponents.TiledObj import TiledObj


class Medusa(TiledObj):
    Medusas: set["Medusa"] = set()

    def __init__(self, start_tile: Vec2[int], looking: Vec2[int]):
        self.looking = looking
        self._position: Vec2[int] = start_tile
        self.position = start_tile
        self.is_moving = False
        Medusa.Medusas.add(self)

    def init(self):
        self.teleport(self.position)

    def on_destroy(self):
        if self in Medusa.Medusas:
            Medusa.Medusas.remove(self)
        super().on_destroy()

    def loop(self):
        pass

    @staticmethod
    def is_looking_to_medusa(pos: Vec2[int], looking: Vec2[int], mirror: bool = False) -> bool:
        if looking == Vec2(0, 0):
            return False
        new_pos = pos + looking

        if Map.instance.is_solid(new_pos):
            return False

        next_obj = TiledObj.AllObjs.get(new_pos.to_tuple, None)
        if next_obj is not None:
            next_obj_type = type(next_obj)
            if next_obj_type is Medusa:
                return True
            elif next_obj_type is Mirror:
                return Medusa.is_looking_to_medusa(
                    new_pos,
                    Vec2(*next_obj.map_light[looking.to_tuple]),
                    True
                )
            if mirror:
                if not next_obj.transparent_after_mirror:
                    return False
            else:
                if not next_obj.transparent:
                    return False

        return Medusa.is_looking_to_medusa(new_pos, looking)

    @staticmethod
    def update_state():
        for medusa in list(Medusa.Medusas):
            if Medusa.is_looking_to_medusa(medusa.position, medusa.looking):
                print("Destroying medusa")
                medusa.item.Destroy()
