import unittest

from src.bot.bot import Bot, ROTATE_45_DEGREE_GENE
from src.const.cell import CellType
from src.const.direction import Direction
from src.world.location import Location
from src.world.world import World


class BotLookupTest(unittest.TestCase):

    def test_lookup_empty(self):
        world = World()
        location = Location(2, 2)
        bot = Bot(location, world)
        world.update_cell(location, bot)
        world.update_cell(Location(3, 1), CellType.EMPTY)
        bot.energy = 77
        bot.direction = Direction.NE
        bot.lookup(0)
        self.assertEqual(77, bot.energy)
        self.assertEqual(Direction.NE, bot.direction)
        self.assertEqual(ROTATE_45_DEGREE_GENE, bot.genes.get_next())
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
        bot.lookup(0)
        self.assertEqual(77, bot.energy)
        self.assertEqual(Direction.E, bot.direction)
        self.assertTrue(isinstance(world.get_cell(bot_location), Bot))
        self.assertEqual(8, bot.genes.get_next())

    def test_peek_poison(self):
        world = World()
        bot_location = Location(2, 2)
        bot = Bot(bot_location, world)
        world.update_cell(bot_location, bot)
        bot.energy = 77
        bot.direction = Direction.E
        poison_location = Location(3, 3)
        world.update_cell(poison_location, CellType.POISON)
        bot.lookup(1)
        self.assertEqual(77, bot.energy)
        self.assertEqual(Direction.E, bot.direction)
        self.assertEqual(CellType.POISON, world.get_cell(poison_location))
        self.assertTrue(isinstance(world.get_cell(bot_location), Bot))
        self.assertEqual(24, bot.genes.get_next())

    def test_peek_wall(self):
        world = World()
        bot_location = Location(1, 1)
        bot = Bot(bot_location, world)
        world.update_cell(bot_location, bot)
        bot.energy = 77
        bot.direction = Direction.E
        bot.lookup(7)
        self.assertEqual(77, bot.energy)
        self.assertEqual(Direction.E, bot.direction)
        self.assertEqual(CellType.WALL, world.get_cell(Location(0, 0)))
        self.assertTrue(isinstance(world.get_cell(bot_location), Bot))
        self.assertEqual(ROTATE_45_DEGREE_GENE, bot.genes.get_next())

    def test_peek_bot(self):
        world = World()
        current_bot_location = Location(3, 4)
        current_bot = Bot(current_bot_location, world)
        world.update_cell(current_bot_location, current_bot)
        current_bot.energy = 77
        current_bot.direction = Direction.NW

        other_bot_location = Location(2, 3)
        other_bot = Bot(other_bot_location, world)
        world.update_cell(other_bot_location, other_bot)

        current_bot.lookup(7)
        self.assertEqual(77, current_bot.energy)
        self.assertEqual(Direction.NW, current_bot.direction)
        self.assertEqual(other_bot, world.get_cell(other_bot_location))
        self.assertEqual(current_bot, world.get_cell(current_bot_location))
        self.assertEqual(ROTATE_45_DEGREE_GENE, current_bot.genes.get_next())


if __name__ == '__main__':
    unittest.main()
