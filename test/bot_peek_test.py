import unittest

from src.bot.bot import Bot, ROTATE_45_DEGREE_GENE
from src.const.cell import CellType
from src.const.direction import Direction
from src.world.location import Location
from src.world.world import World


class BotPeekTest(unittest.TestCase):

    def test_peek_empty(self):
        world = World()
        location = Location(2, 2)
        bot = Bot(location, world)
        world.update_cell(location, bot)
        world.update_cell(Location(2, 1), CellType.EMPTY)
        bot.energy = 77
        bot.direction = Direction.NE
        bot.peek(0)
        self.assertEqual(77, bot.energy)
        self.assertEqual(Direction.NE, bot.direction)
        self.assertEqual(25, bot.genes.get_next())
        self.assertTrue(isinstance(world.get_cell(location), Bot))

    def test_peek_food(self):
        world = World()
        bot_location = Location(2, 2)
        bot = Bot(bot_location, world)
        world.update_cell(bot_location, bot)
        bot.energy = 77
        bot.direction = Direction.E
        food_location = Location(3, 2)
        world.update_cell(food_location, CellType.FOOD)
        bot.peek(0)
        self.assertEqual(77, bot.energy)
        self.assertEqual(Direction.E, bot.direction)
        self.assertTrue(isinstance(world.get_cell(bot_location), Bot))
        self.assertEqual(0, bot.genes.get_next())

    def test_peek_poison(self):
        world = World()
        bot_location = Location(2, 2)
        bot = Bot(bot_location, world)
        world.update_cell(bot_location, bot)
        bot.energy = 77
        bot.direction = Direction.E
        poison_location = Location(3, 3)
        world.update_cell(poison_location, CellType.POISON)
        bot.peek(1)
        self.assertEqual(77, bot.energy)
        self.assertEqual(Direction.E, bot.direction)
        self.assertEqual(CellType.FOOD, world.get_cell(poison_location))
        self.assertTrue(isinstance(world.get_cell(bot_location), Bot))
        self.assertEqual(1, bot.genes.get_next())

    def test_peek_wall(self):
        world = World()
        bot_location = Location(1, 1)
        bot = Bot(bot_location, world)
        world.update_cell(bot_location, bot)
        bot.energy = 77
        bot.direction = Direction.E
        bot.peek(7)
        self.assertEqual(77, bot.energy)
        self.assertEqual(Direction.E, bot.direction)
        self.assertEqual(CellType.WALL, world.get_cell(Location(0, 0)))
        self.assertTrue(isinstance(world.get_cell(bot_location), Bot))
        self.assertEqual(ROTATE_45_DEGREE_GENE, bot.genes.get_next())

    def test_peek_bot(self):
        pass


if __name__ == '__main__':
    unittest.main()
