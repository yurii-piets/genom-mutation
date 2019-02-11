from enum import Enum


class Effect(Enum):
    POISONED = 0
    EMPTY = 1
    WALL = 2
    FOOD = 3
    MEET_OTHER_BOT = 4
    DIE = 5
    OK = 6
