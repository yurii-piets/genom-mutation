from random import randint

from src.const.cell import CellType
from src.const.config import MAX_POISON, MAX_FOOD, WORLD_WIDTH, WORLD_HEIGHT
from src.world.location import Location


class World:

    def __init__(self):
        self.cells = {}
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
    return 0 <= location.x <= WORLD_WIDTH and 0 <= location.y <= WORLD_HEIGHT


def raise_out_of_world_range_exception(location):
    raise Exception("Requested location: " + str(location) + " is out of world range")

