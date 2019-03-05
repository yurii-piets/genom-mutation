import datetime
import time

from src.bot.bot import Bot
from src.const.effect import Effect
from src.world.world import random_location

BOTS_COUNT = 64


class BootPool:

    def __init__(self, world):
        self.world = world
        self.bots = self.init_bots(world)
        self.generation = 0

    def init_bots(self, world):
        bots = set()
        for i in range(BOTS_COUNT):
            location = random_location()
            while not world.is_free(location):
                location = random_location()
            bot = Bot(location, world, self)
            world.put(location, bot)
            bots.add(bot)
        return bots

    def bot_dead(self, bot):
        self.bots.remove(bot)

    def bots_make_steps(self):
        dead_bots = set()
        for bot in self.bots:
            effect = bot.step()
            if effect == Effect.DIE:
                dead_bots.add(bot)
        for bot in dead_bots:
            bot.die()

    def bots_make_clones(self):
        new_bots = set()
        for bot in self.bots:
            if bot.is_alive():
                for i in range(7):
                    mutated_bot = bot.clone_with_mutation()
                    new_bots.add(mutated_bot)
                    location = random_location()
                    while not self.world.is_free(location):
                        location = random_location()
                    mutated_bot.location = location
                    self.world.put(location, bot)

        self.bots.update(new_bots)
        new_bots = set()
        # for bot in self.bots:
        #     if len(new_bots) + self.bots_count() == BOTS_COUNT:
        #         break
        #     mutated_bot = bot.clone_with_mutation()
        #     new_bots.add(mutated_bot)
        #     location = random_location()
        #     while not self.world.is_free(location):
        #         location = random_location()
        #     mutated_bot.location = location
        #     self.world.put(location, bot)
        # self.bots.update(new_bots)
        self.generation += 1

    def bots_count(self):
        return len(self.bots)
