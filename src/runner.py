import datetime

from src.bot.boot_pool import BootPool
from src.world.world import World
import time


def run():
    world = World()
    bot_pool = BootPool(world)
    while True:
        if bot_pool.bots_count() > 8:
            # print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Steps")
            bot_pool.bots_make_steps()
        else:
            # print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Clones")
            bot_pool.bots_make_clones()

            # print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Fill poison and food")
            world.fill_poison_and_food()
            # print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| " + str(
            #     bot_pool.generation))


run()
