import time

from src.const.config import MIN_BOTS

SLEEP_BETWEEN_STEPS = 0.3


def run(world, bot_pool):
    while True:
        if len(bot_pool) > MIN_BOTS:
            bot_pool.execute_bots_commands()
        else:
            bot_pool.clone_bots()
            world.fill_food()
            world.fill_poison()
        time.sleep(SLEEP_BETWEEN_STEPS)
