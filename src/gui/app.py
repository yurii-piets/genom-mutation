import pyglet

from src.bot.boot_pool import BootPool
from src.bot.bot import Bot
from src.gui.cell import cell_color_by_type
from src.world.world import World, WORLD_HEIGHT, WORLD_WIDTH

MAX_X = 1780
MAX_Y = 889
MARGIN = 2
DEFAULT_SIZE = 25


class ShapeWindow(pyglet.window.Window):

    def __init__(self, *args, **kwargs):
        pyglet.window.Window.__init__(self, *args, **kwargs)
        self.set_size(MAX_X, MAX_Y)
        self.world = World()
        self.bot_pool = BootPool(self.world)

    def on_draw(self):
        self.draw_world(self.world)
        self.draw_generation(self.bot_pool.generation)

    def move(self, *args):
        if self.bot_pool.bots_count() > 8:
            self.bot_pool.bots_make_steps()
        else:
            self.bot_pool.bots_make_clones()
            self.world.fill_poison_and_food()

    def draw_world(self, world):
        for i in range(0, WORLD_HEIGHT):
            for j in range(0, WORLD_WIDTH):
                self.draw_cell(j, i, world.board[i][j])

    def draw_cell(self, relative_x, relative_y, cell_type):
        absolute_x = 0
        if relative_x != 0:
            absolute_x = relative_x * (DEFAULT_SIZE + MARGIN)
        absolute_x = absolute_x + DEFAULT_SIZE

        absolute_y = 0
        if relative_y != 0:
            absolute_y = relative_y * (DEFAULT_SIZE + MARGIN)
        absolute_y = MAX_Y - absolute_y

        self.draw_rectangle(absolute_x, absolute_y, cell_color_by_type(cell_type))
        if isinstance(cell_type, Bot):
            self.draw_text(cell_type.energy, absolute_x, absolute_y)

    def draw_generation(self, generation):
        label = pyglet.text.Label("Generation: " + str(generation),
                                  font_name='Roboto',
                                  font_size=14,
                                  x=28, y=3)
        label.draw()

    def draw_rectangle(self, absolute_x, absolute_y, color, size=DEFAULT_SIZE):
        pyglet.graphics.draw(4, pyglet.gl.GL_QUADS,
                             ('v2i', (absolute_x, absolute_y, absolute_x - size, absolute_y, absolute_x - size,
                                      absolute_y - size, absolute_x, absolute_y - size)),
                             ('c3B', color))

    def draw_text(self, text, absolute_x, absolute_y):
        label = pyglet.text.Label(str(text),
                                  font_name='Roboto',
                                  font_size=14,
                                  x=absolute_x - DEFAULT_SIZE + MARGIN, y=absolute_y - DEFAULT_SIZE + MARGIN)
        label.draw()


shape_window = ShapeWindow()
pyglet.clock.schedule_interval(shape_window.move, 0.3)
pyglet.app.run()
