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

    def test_put_when_empty(self):
        world = World()
        result = world.put_cell(Location(1, 1), CellType.FOOD)
        self.assertTrue(result)

    def test_put_when_not_empty(self):
        world = World()
        world.put_cell(Location(1, 1), CellType.FOOD)
        result = world.put_cell(Location(1, 1), CellType.FOOD)
        self.assertFalse(result)

    def test_put_when_out_of_range(self):
        world = World()
        with self.assertRaises(Exception):
            world.put_cell(Location(999999, 988888), CellType.POISON)


if __name__ == '__main__':
    unittest.main()
