import datetime
import time

from src.bot.boot_pool import BootPool
from src.const.cell import CellType
from src.const.config import MIN_BOTS
from src.world.world import World

SLEEP_BETWEEN_STEPS = 0.3


def print_genes(bots):
    for bot in bots:
        print("Bot g: " + str(bot.generation) + ", a: " + str(bot.generations_alive) + ", g: " + str(bot.genes.genes))


def run(world, bot_pool):
    while True:
        if len(bot_pool) > MIN_BOTS:
            bot_pool.execute_bots_commands()
        else:
            bot_pool.clone_bots()
            print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Generation: " + str(bot_pool.generation))
            print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Longest bot generation: " + str(max(value.generation for value in bot_pool.bots)))
            print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Bots count: " + str(len(bot_pool)))
            print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "| Left food: "
                  + str(sum(value == CellType.FOOD for value in world.cells.values())) + " , poison: "
                  + str(sum(value == CellType.POISON for value in world.cells.values())))
            print_genes(bot_pool.bots)
            world.fill_food()
            world.fill_poison()
        time.sleep(SLEEP_BETWEEN_STEPS)


if __name__ == '__main__':
    SLEEP_BETWEEN_STEPS = 0
    world = World()
    bot_pool = BootPool(world)
    run(world, bot_pool)