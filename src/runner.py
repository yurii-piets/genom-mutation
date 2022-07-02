import time

from src.bot.boot_pool import BootPool
from src.const.config import MIN_BOTS
from src.world.world import World

SLEEP_BETWEEN_STEPS = 0.3


def run(world, bot_pool):
    while True:
        if len(bot_pool) > MIN_BOTS:
            bot_pool.execute_bots_commands()
        else:
            bot_pool.clone_bots()
            world.fill_food()
            world.fill_poison()
        # time.sleep(SLEEP_BETWEEN_STEPS)


if __name__ == '__main__':
    SLEEP_BETWEEN_STEPS = 0
    world = World()
    bot_pool = BootPool(world)
    run(world, bot_pool)
