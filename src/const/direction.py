from enum import Enum


class Direction(Enum):
    N = 0,
    NE = 1,
    E = 2,
    SE = 3,
    S = 4,
    SW = 5,
    W = 6,
    NW = 7


directions_vectors = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
directions = [Direction.N, Direction.NE, Direction.E, Direction.SE, Direction.S, Direction.SW, Direction.W,
              Direction.NW]

DIRECTIONS_COUNT = len(directions_vectors)


def get_direction_vector(start, index):
    final_index = (start + index) % DIRECTIONS_COUNT
    return directions_vectors[final_index]


def get_direction(start, index):
    final_index = (start.value[0] + index) % DIRECTIONS_COUNT
    return directions[final_index]
