from src.bot.boot_pool import BootPool
from src.world.world import World


def run():
    world = World()
    bot_pool = BootPool(world)
    while True:
        while bot_pool.bots_count() > 8:
            bot_pool.bots_make_steps()
        bot_pool.bots_make_clones()
        world.fill_poison_and_food()


run()
