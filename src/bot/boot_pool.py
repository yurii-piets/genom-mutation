from random import shuffle

from src.bot.bot import Bot
from src.const.cell import CellType
from src.const.config import BOTS_COUNT, MIN_BOTS, BOTS_CLONES, ENERGY
from src.data.data_exporter import CsvDataExporter


class BootPool:

    def __init__(self, world):
        self.world = world
        self.bots = create_bots(world)
        self.epoch = 0
        self.ticks = 0
        self.data_exporter = CsvDataExporter()

    def execute_bots_commands(self):
        dead_bots = set()
        bots_as_list = list(self.bots)
        shuffle(bots_as_list)
        for bot in bots_as_list:
            if len(self.bots) - len(dead_bots) <= MIN_BOTS:
                break
            bot.execute_commands()
            if not bot.is_alive():
                dead_bots.add(bot)

        for bot in dead_bots:
            self.world.update_cell(bot.location, CellType.EMPTY)
            self.bots.remove(bot)
            self.data_exporter.save_bot_epoch_ticks(self.epoch, bot.ticks)
        self.ticks += 1

    def clone_bots(self):
        new_bots = set()

        for bot in self.bots:
            self.data_exporter.save_bot_epoch_ticks(self.epoch, bot.ticks)
            if bot.energy < ENERGY:
                bot.energy = ENERGY
            for i in range(BOTS_CLONES):
                cloned_bot = bot.clone()
                cloned_bot.created_epoch = self.epoch
                location = self.world.rand_free_location()
                cloned_bot.location = location
                self.world.put_cell(location, cloned_bot)
                new_bots.add(cloned_bot)

        self.bots.update(new_bots)
        self.data_exporter.save_epoch_ticks(self.epoch, self.ticks)
        self.epoch += 1
        self.ticks = 0

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
