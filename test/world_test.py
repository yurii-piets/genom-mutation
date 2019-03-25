from src.const.cell import CellType
from src.world.location import Location
from src.world.world import World
import unittest


class TestStringMethods(unittest.TestCase):

    def test_get_when_not_exist(self):
        world = World()
        self.assertEqual(world.get_cell(Location(1, 1)), CellType.EMPTY)

    def test_get_when_out_of_range(self):
        world = World()
        with self.assertRaises(Exception):
            world.get_cell(Location(1000000, 1000000))

    def test_get_wall(self):
        world = World()
        location = Location(0, 0)
        result = world.get_cell(location)
        self.assertEqual(CellType.WALL, result)

    def test_put(self):
        world = World()
        location = Location(2, 3)
        world.put_cell(location, CellType.EMPTY)
        self.assertEqual(CellType.EMPTY, world.get_cell(location))
        world.put_cell(location, CellType.FOOD)
        self.assertEqual(CellType.FOOD, world.get_cell(location))
        result = world.put_cell(location, CellType.EMPTY)
        self.assertFalse(result)

    def test_put_on_wall(self):
        world = World()
        location = Location(0, 0)
        result = world.put_cell(location, CellType.POISON)
        self.assertFalse(result)

    def test_put_when_empty(self):
        world = World()
        result = world.put_cell(Location(1, 1), CellType.FOOD)
        self.assertTrue(result)

    def test_put_empty_when_not_exist(self):
        world = World()
        location = Location(1, 1)
        world.put_cell(location, CellType.EMPTY)

    def test_put_empty_when_empty(self):
        world = World()
        location = Location(1, 1)
        world.put_cell(location, CellType.EMPTY)
        world.put_cell(location, CellType.EMPTY)

    def test_put_when_not_empty(self):
        world = World()
        world.put_cell(Location(1, 1), CellType.FOOD)
        result = world.put_cell(Location(1, 1), CellType.FOOD)
        self.assertFalse(result)

    def test_put_when_out_of_range(self):
        world = World()
        with self.assertRaises(Exception):
            world.put_cell(Location(999999, 988888), CellType.POISON)

    def test_update_when_is_free(self):
        world = World()
        old_value = world.update_cell(Location(1, 1), CellType.POISON)
        self.assertIsNone(old_value)

    def test_update_when_is_not_free(self):
        world = World()
        world.put_cell(Location(1, 1), CellType.FOOD)
        old_value = world.update_cell(Location(1, 1), CellType.POISON)
        self.assertEqual(old_value, CellType.FOOD)

    def test_update_empty_when_not_exist(self):
        world = World()
        location = Location(1, 1)
        world.update_cell(location, CellType.EMPTY)

    def test_update_empty_when_empty(self):
        world = World()
        location = Location(1, 1)
        world.update_cell(location, CellType.EMPTY)
        world.update_cell(location, CellType.EMPTY)

    def test_update(self):
        world = World()
        location = Location(2, 3)
        world.update_cell(location, CellType.EMPTY)
        self.assertEqual(CellType.EMPTY, world.get_cell(location))
        world.update_cell(location, CellType.FOOD)
        self.assertEqual(CellType.FOOD, world.get_cell(location))
        world.update_cell(location, CellType.EMPTY)
        self.assertEqual(CellType.EMPTY, world.get_cell(location))

    def test_update_on_wall(self):
        world = World()
        location = Location(0, 0)
        result = world.update_cell(location, CellType.POISON)
        self.assertEqual(CellType.WALL, result)


if __name__ == '__main__':
    unittest.main()
