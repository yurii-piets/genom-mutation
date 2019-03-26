import unittest

from src.bot.bot import Bot
from src.const.cell import CellType
from src.const.direction import Direction
from src.world.location import Location
from src.world.world import World


class BotMoveTest(unittest.TestCase):

    def test_move_to_empty(self):
        world = World()
        old_location = Location(2, 2)
        bot = Bot(old_location, world)
        world.update_cell(old_location, bot)
        expected_future_location = Location(2, 1)
        world.update_cell(expected_future_location, CellType.EMPTY)
        bot.direction = Direction.N
        bot.move(0)
        self.assertTrue(isinstance(world.get_cell(expected_future_location), Bot))
        self.assertEqual(CellType.EMPTY, world.get_cell(old_location))
        self.assertEqual(Direction.N, bot.direction)

    def test_move_to_food(self):
        world = World()
        old_location = Location(2, 2)
        expected_future_location = Location(3, 1)
        world.update_cell(expected_future_location, CellType.FOOD)
        bot = Bot(old_location, world)
        world.update_cell(old_location, bot)
        bot.direction = Direction.NE
        bot.energy = 11
        bot.move(0)
        self.assertTrue(isinstance(world.get_cell(expected_future_location), Bot))
        self.assertEqual(CellType.EMPTY, world.get_cell(old_location))
        self.assertEqual(Direction.NE, bot.direction)
        self.assertEqual(21, bot.energy)

    def test_move_to_poison(self):
        world = World()
        old_location = Location(3, 1)
        expected_future_location = Location(4, 2)
        world.update_cell(expected_future_location, CellType.POISON)
        bot = Bot(old_location, world)
        world.update_cell(old_location, bot)
        bot.direction = Direction.E
        bot.move(1)
        self.assertEqual(CellType.POISON, world.get_cell(expected_future_location))
        self.assertEqual(CellType.EMPTY, world.get_cell(old_location))
        self.assertEqual(Direction.E, bot.direction)

    def test_move_to_bot(self):
        world = World()
        other_bot_location = Location(2, 4)
        current_bot_location = Location(1, 3)
        other_bot = Bot(other_bot_location, world)
        current_bot = Bot(current_bot_location, world)
        world.update_cell(other_bot_location, other_bot)
        world.update_cell(current_bot_location, current_bot)
        current_bot.direction = Direction.S
        current_bot.energy = 10
        current_bot.move(7)
        self.assertEqual(current_bot, world.get_cell(current_bot_location))
        self.assertEqual(other_bot, world.get_cell(other_bot_location))
        self.assertEqual(Direction.S, current_bot.direction)
        self.assertEqual(11, current_bot.energy)
        self.assertEqual(25, current_bot.genes.get_next())

    def test_move_to_wall(self):
        world = World()
        old_location = Location(1, 1)
        bot = Bot(old_location, world)
        world.update_cell(old_location, bot)
        bot.direction = Direction.NW
        bot.move(0)
        self.assertEqual(CellType.WALL, world.get_cell(Location(0, 0)))
        self.assertTrue(isinstance(world.get_cell(old_location), Bot))
        self.assertEqual(Direction.NW, bot.direction)
        self.assertEqual(25, bot.genes.get_next())


if __name__ == '__main__':
    unittest.main()
