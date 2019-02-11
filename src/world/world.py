from random import randint

from src.const.cell import CellType
from src.world.location import Location

WORLD_WIDTH = 64
WORLD_HEIGHT = 128


class World:
    def __init__(self):
        self.board = random_board()

    def get(self, location):
        if is_in_range(location):
            return self.board[location.x][location.y]
        return CellType.WALL

    def put(self, location, obj):
        if self.is_free(location):
            self.force_put(location, obj)
            return True
        return False

    def is_free(self, location):
        return self.board[location.x][location.y] == CellType.EMPTY

    def force_put(self, location, obj):
        self.board[location.x][location.y] = obj

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
    for i in range(WORLD_WIDTH):
        sub_board = []
        for j in range(WORLD_HEIGHT):
            sub_board.append(CellType.EMPTY)
        board.append(sub_board)
    return board


def random_location():
    x = randint(0, WORLD_WIDTH - 1)
    y = randint(0, WORLD_HEIGHT - 1)
    return Location(x, y)
