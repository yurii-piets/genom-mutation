from src.bot.boot_pool import BootPool
from src.world.world import World


def run():
    world = World()
    bot_pool = BootPool(world)
    print(world)
    print("--------------------------------------------------------------------------------------------------------------------------------")
    while True:
        while bot_pool.bots_count() > 8:
            bot_pool.bots_make_steps()
            print(world)
        bot_pool.bots_make_clones()
        print("---------------------------------------------------------------------------------------------------------------------------")


run()
