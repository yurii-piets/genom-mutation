from random import randint

from src.const.cell import CellType
from src.world.location import Location

WORLD_WIDTH = 66
WORLD_HEIGHT = 33

MAX_FOOD = 120
MAX_POISON = 50


class World:
    def __init__(self):
        self.food_amount = 0
        self.poison_amount = 0
        self.board = random_board()
        self.fill_poison_and_food()

    def get(self, location):
        if is_in_range(location):
            return self.board[location.y][location.x]
        return CellType.WALL

    def put(self, location, obj):
        if self.is_free(location):
            self.force_put(location, obj)
            return True
        return False

    def is_free(self, location):
        return self.board[location.y][location.x] == CellType.EMPTY

    def force_put(self, location, obj):
        self.board[location.y][location.x] = obj

    def fill_poison_and_food(self):
        self.fill_poison()
        self.fill_food()

    def fill_poison(self):
        while self.poison_amount < MAX_POISON:
            location = random_location()
            while not self.is_free(location):
                location = random_location()
            self.force_put(location, CellType.POISON)
            self.poison_amount += 1

    def fill_food(self):
        while self.food_amount < MAX_FOOD:
            location = random_location()
            while not self.is_free(location):
                location = random_location()
            self.force_put(location, CellType.FOOD)
            self.food_amount += 1

    def __repr__(self):
        board_repr = ""
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == CellType.EMPTY:
                    board_repr += "."
                else:
                    board_repr += repr(self.board[i][j])
            board_repr += "\n"
        return board_repr

    def __del__(self):
        self.board = []


def is_in_range(location):
    return 0 <= location.x < WORLD_WIDTH and 0 <= location.y < WORLD_HEIGHT


def random_board():
    board = []
    for i in range(WORLD_HEIGHT):
        sub_board = []
        for j in range(WORLD_WIDTH):
            if i == 0 or i == WORLD_HEIGHT - 1 or j == 0 or j == WORLD_WIDTH - 1:
                sub_board.append(CellType.WALL)
            else:
                sub_board.append(CellType.EMPTY)
        board.append(sub_board)
    return board


def random_location():
    x = randint(0, WORLD_WIDTH - 1)
    y = randint(0, WORLD_HEIGHT - 1)
    return Location(x, y)
