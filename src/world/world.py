from random import randint

from src.const.cell import CellType
from src.const.config import MAX_POISON, MAX_FOOD, WORLD_WIDTH, WORLD_HEIGHT
from src.world.location import Location, random_location


class World:

    def __init__(self):
        self.cells = {}
        put_walls(self)
        self.fill_food()
        self.fill_poison()

    def get_cell(self, location):
        if not is_in_range(location):
            raise_out_of_world_range_exception(location)
        cell_object = self.cells.get(location.to_tuple())
        if self.is_free(location):
            return CellType.EMPTY
        return cell_object

    def put_cell(self, location, obj):
        if not is_in_range(location):
            raise_out_of_world_range_exception(location)
        if not self.is_free(location):
            return False
        if obj != CellType.EMPTY:
            self.cells[location.to_tuple()] = obj
        return True

    def update_cell(self, location, obj):
        if not is_in_range(location):
            raise_out_of_world_range_exception(location)
        location_tuple = location.to_tuple()
        old_value = self.cells.get(location_tuple)
        if obj == CellType.EMPTY:
            if location.to_tuple() in self.cells:
                self.cells.pop(location.to_tuple())
        else:
            self.cells[location.to_tuple()] = obj
        return old_value

    def fill_food(self):
        while self.food_amount() < MAX_FOOD:
            location = self.rand_free_location()
            self.update_cell(location, CellType.FOOD)

    def fill_poison(self):
        while self.poison_amount() < MAX_POISON:
            location = self.rand_free_location()
            self.update_cell(location, CellType.POISON)

    def is_free(self, location):
        if not is_in_range(location):
            raise_out_of_world_range_exception(location)
        cell_object = self.cells.get(location.to_tuple())
        return cell_object is None or cell_object == CellType.EMPTY

    def rand_free_location(self):
        if len(self.cells) >= (WORLD_HEIGHT - 1) * (WORLD_WIDTH - 1):
            raise Exception("No free locations in the world has left")
        location = random_location()
        while not self.is_free(location):
            location = random_location()
        return location

    def food_amount(self):
        return sum(value == CellType.FOOD for value in self.cells.values())

    def poison_amount(self):
        return sum(value == CellType.POISON for value in self.cells.values())


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
