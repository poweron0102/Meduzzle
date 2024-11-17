from Components.Sprite import Sprite, convert_to_grayscale
from Geometry import Vec2
from UserComponents.Map import Map
from UserComponents.Mirror import Mirror
from UserComponents.Pushable import Pushable
from UserComponents.TiledObj import TiledObj


class PetrifiedMedusa(Pushable):
    pass


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

    def petrify(self):
        item = self.item
        pos: Vec2[int] = self.position
        self.Destroy()
        sprite = self.GetComponent(Sprite)
        item.AddComponent(PetrifiedMedusa(pos))
        for i in range(10):
            sprite.image = convert_to_grayscale(sprite.image, i / 10)
            yield 0.2

    @staticmethod
    def is_looking_to_medusa(
            pos: Vec2[int],
            looking: Vec2[int],
            mirror: bool = False,
            passed: set[tuple[tuple[int, int], tuple[int, int]]] = None
    ):
        if looking == Vec2(0, 0):
            return False

        if passed is None:
            passed = set()
        if (pos.to_tuple, looking.to_tuple) in passed:
            return False
        passed.add((pos.to_tuple, looking.to_tuple))

        new_pos = pos + looking

        if Map.instance.is_solid(new_pos):
            return False

        next_obj = TiledObj.AllObjs.get(new_pos.to_tuple, None)
        if next_obj is not None:
            if isinstance(next_obj, Medusa):
                return True
            if isinstance(next_obj, Mirror):
                return Medusa.is_looking_to_medusa(new_pos, Vec2(*next_obj.map_light[looking.to_tuple]), True, passed)
            if mirror:
                if not next_obj.transparent_after_mirror:
                    return False
            else:
                if not next_obj.transparent:
                    return False

        return Medusa.is_looking_to_medusa(new_pos, looking, mirror, passed)

    @staticmethod
    def update_state():
        for medusa in list(Medusa.Medusas):
            if Medusa.is_looking_to_medusa(medusa.position, medusa.looking):
                medusa.game.scheduler.add_generator(medusa.petrify())
