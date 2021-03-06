from random import randint, sample

from src.bot.bot import Bot
from src.const.cell import CellType
from src.const.config import BOTS_COUNT, MIN_BOTS, BOTS_CLONES


class BootPool:

    def __init__(self, world):
        self.generation = 0
        self.world = world
        self.bots = create_bots(world)

    def execute_bots_commands(self):
        dead_bots = set()
        for bot in self.bots:
            if BOTS_COUNT - len(dead_bots) <= MIN_BOTS:
                break
            bot.execute_commands()
            if not bot.is_alive():
                dead_bots.add(bot)

        for bot in dead_bots:
            self.world.update_cell(bot.location, CellType.EMPTY)
            self.bots.remove(bot)

    def clone_bots(self):
        self.generation += 1
        new_bots = set()

        bots_to_mutate = sample(self.bots, 1)

        for bot in self.bots:
            bot.generations_alive += 1
            future_energy = randint(40, 80)
            if future_energy > bot.energy:
                bot.energy = future_energy
            if bot in bots_to_mutate:
                bot.mutate()
            else:
                bot.generation += 1
            for i in range(BOTS_CLONES):
                cloned_bot = bot.clone()
                location = self.world.rand_free_location()
                cloned_bot.location = location
                self.world.put_cell(location, cloned_bot)
                new_bots.add(cloned_bot)

        self.bots.update(new_bots)

    def __len__(self):
        return len(self.bots)


def create_bots(world):
    bots = set()
    for i in range(BOTS_COUNT):
        location = world.rand_free_location()
        bot = Bot(location, world)
        world.put_cell(location, bot)
        bots.add(bot)
    return bots
