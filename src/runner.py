import time
from enum import Enum

from src.bot.boot_pool import BootPool
from src.const.config import MIN_BOTS, MIN_FOOD
from src.world.world import World

SLEEP_BETWEEN_STEPS = 0.3

class Profile(Enum):
    CONSOLE = 0,
    UI = 1


def run(world, bot_pool, profile):
    while True:
        if len(bot_pool) > MIN_BOTS:
            if world.food_amount() <= MIN_FOOD:
                world.fill_food()
            if world.poison_amount() <= MIN_FOOD:
                world.fill_poison()
            bot_pool.execute_bots_commands()
        else:
            bot_pool.clone_bots()
            world.fill_food()
            world.fill_poison()

        if profile == Profile.UI:
            time.sleep(1.0/60.0)


if __name__ == '__main__':
    SLEEP_BETWEEN_STEPS = 0
    world = World()
    bot_pool = BootPool(world)
    run(world, bot_pool, profile=Profile.CONSOLE)
