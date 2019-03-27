import datetime
import time

from src.bot.boot_pool import BootPool
from src.const.cell import CellType
from src.const.config import MIN_BOTS
from src.world.world import World


def run(world, bot_pool):
    while True:
        if len(bot_pool) > MIN_BOTS:
            bot_pool.execute_bots_commands()
        else:
            bot_pool.clone_bots()
            print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Bots count: " + str(len(bot_pool)))
            print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Generation: " + str(bot_pool.generation))
            print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Longest bot generation: " + str(max(value.generation for value in bot_pool.bots)))
            print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Longest genes: " + str(max(len(value.genes) for value in bot_pool.bots)))
            world.fill_food()
            world.fill_poison()
        time.sleep(0.8)


#world = World()
#bot_pool = BootPool(world)
#run(world, bot_pool)

# print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Steps")
# print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Fill food: "
#      + str(sum(value == CellType.FOOD for value in world.cells.values())) + " , poison: "
#      + str(sum(value == CellType.POISON for value in world.cells.values())))
#            print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Clones")