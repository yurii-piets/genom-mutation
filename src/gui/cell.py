from src.bot.bot import Bot
from src.const.cell import CellType


def cell_color_by_type(cell_type):
    if cell_type == CellType.EMPTY:
        return 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21
    if cell_type == CellType.WALL:
        return 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90
    if isinstance(cell_type, Bot):
        return 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255
    if cell_type == CellType.POISON:
        return 255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0, 0
    if cell_type == CellType.FOOD:
        return 0, 255, 0, 0, 255, 0, 0, 255, 0, 0, 255, 0
