import unittest

from src.bot.bot import Bot
from src.const.direction import Direction


class BotMoveTest(unittest.TestCase):

    def test_rotate_from_n_with_0(self):
        bot = Bot(None, None)
        bot.direction = Direction.N
        bot.rotate(0)
        self.assertEqual(Direction.NE, bot.direction)

    def test_rotate_from_n_with_6(self):
        bot = Bot(None, None)
        bot.direction = Direction.N
        bot.rotate(6)
        self.assertEqual(Direction.NW, bot.direction)

    def test_rotate_from_ne_with_1(self):
        bot = Bot(None, None)
        bot.direction = Direction.NE
        bot.rotate(1)
        self.assertEqual(Direction.SE, bot.direction)

    def test_rotate_from_nw_with_6(self):
        bot = Bot(None, None)
        bot.direction = Direction.NW
        bot.rotate(6)
        self.assertEqual(Direction.W, bot.direction)
