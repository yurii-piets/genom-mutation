import datetime
import time

from src.bot.boot_pool import BootPool
from src.const.cell import CellType
from src.const.config import MIN_BOTS
from src.world.world import World


def run(world, bot_pool):
    while True:
        if len(bot_pool) > MIN_BOTS:
            # print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Steps")
            bot_pool.execute_bots_commands()
        else:
            print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Clones")
            bot_pool.clone_bots()
            print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Bots count: " + str(len(bot_pool)))
            world.fill_food()
            world.fill_poison()
            print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Fill food: "
                  + str(sum(value == CellType.FOOD for value in world.cells.values())) + " , poison: "
                  + str(sum(value == CellType.POISON for value in world.cells.values())))
            print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Generation: " + str(
                bot_pool.generation))
        time.sleep(0.8)


# world = World()
# bot_pool = BootPool(world)
# run(world, bot_pool)
