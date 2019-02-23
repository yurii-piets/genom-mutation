from enum import Enum


class CellType(Enum):
    FOOD = 1
    POISON = 2
    WALL = 3
    BOT = 4
    EMPTY = 5