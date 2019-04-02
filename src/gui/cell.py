from src.bot.bot import Bot
from src.const.cell import CellType


def cell_color_by_type(cell_type):
    if cell_type == CellType.EMPTY:
        return 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21
    if cell_type == CellType.WALL:
        return 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90
    if isinstance(cell_type, Bot):
        blue = 255
        shade = 153 - ((cell_type.generation % 51) * 50)
        if shade <= 0:
            blue = 255 - (((cell_type.generation % 51) * 50) % 256)
            shade = 0
        else:
            shade %= 154
        return shade, shade, blue, shade, shade, blue, shade, shade, blue, shade, shade, blue
    if cell_type == CellType.POISON:
        return 255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0
    if cell_type == CellType.FOOD:
        return 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0


colors = [(153, 153, 255), (102, 102, 255), (51, 51, 255),
          (0, 0, 255), (0, 0, 204), (0, 0, 153), (0, 0, 102), (0, 0, 51)]
