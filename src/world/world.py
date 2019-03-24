from random import randint

from src.const.cell import CellType
from src.const.config import MAX_POISON, MAX_FOOD, WORLD_WIDTH, WORLD_HEIGHT
from src.world.location import Location


class World:

    def __init__(self):
        self.cells = {}
        put_walls(self)
        self.food_amount = 0
        self.poison_amount = 0

    def get_cell(self, location):
        if not is_in_range(location):
            raise_out_of_world_range_exception(location)
        cell_object = self.cells.get(location.to_tuple())
        if cell_object is None:
            return CellType.EMPTY
        return cell_object

    def put_cell(self, location, obj):
        if not is_in_range(location):
            raise_out_of_world_range_exception(location)
        if self.get_cell(location) == CellType.EMPTY:
            self.cells[location.to_tuple()] = obj
            return True
        return False


def is_in_range(location):
    return 0 <= location.x <= WORLD_WIDTH - 1 and 0 <= location.y <= WORLD_HEIGHT - 1


def raise_out_of_world_range_exception(location):
    raise Exception("Requested location: " + str(location) + " is out of world range")


def put_walls(world):
    for i in range(0, WORLD_WIDTH):
        world.put_cell(Location(i, 0), CellType.WALL)
        world.put_cell(Location(i, WORLD_HEIGHT - 1), CellType.WALL)

    for i in range(0, WORLD_HEIGHT):
        world.put_cell(Location(0, i), CellType.WALL)
        world.put_cell(Location(WORLD_WIDTH - 1, i), CellType.WALL)
