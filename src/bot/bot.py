from random import randint

from src.const.cell import CellType
from src.const.direction import Direction, get_direction_vector, get_direction
from src.const.effect import Effect
from src.bot.genes import Genes, HIGHEST_GENE
from src.world.world import is_in_range


class Bot:

    def __init__(self, location, world, bot_pool, genes=Genes()):
        self.location = location
        self.genes = genes
        self.world = world
        self.bot_pool = bot_pool
        self.energy = randint(50, 90)
        self.command_pointer = 0
        self.direction = Direction.N

    def is_alive(self):
        return self.energy > 0

    def mutate(self):
        self.genes.mutate()

    def clone_with_mutation(self):
        bot = Bot(None, self.world, self.bot_pool, self.genes)
        bot.mutate()
        return bot

    # ------------------------------------------------------ STEP ------------------------------------------------------

    def step(self):
        for i in range(10):
            actual_command = self.genes.get_next()
            if actual_command < 8:
                effect = self.move(actual_command)
                if self.energy <= 0:
                    return Effect.DIE
                return effect
            elif actual_command < 16:
                self.peek(actual_command)
                break
            elif actual_command < 24:
                self.lookup(actual_command)
            elif actual_command < 32:
                self.rotate(actual_command)
                self.genes.shift_pointer(1)
            elif actual_command <= HIGHEST_GENE:
                self.genes.shift_pointer(actual_command)

            if self.energy <= 0:
                return Effect.DIE
        return Effect.OK

    def move(self, command):
        self.energy -= 1
        direction = get_direction_vector(self.direction.value[0], command)
        new_location = self.location.transform(direction)
        effect = self.perform_move(new_location)
        if effect != Effect.POISONED:
            self.genes.shift_pointer(1)
        else:
            self.world.put(self.location, CellType.POISON)
            return Effect.DIE

    def perform_move(self, new_location):
        new_location_obj = self.world.get(new_location)
        if new_location_obj == CellType.FOOD or new_location_obj == CellType.POISON:
            old_location = self.location
            self.location = new_location
            self.world.force_put(old_location, CellType.EMPTY)
            return self.eat(new_location_obj)
        elif new_location_obj == CellType.EMPTY:
            old_location = self.location
            self.location = new_location
            self.world.force_put(old_location, CellType.EMPTY)
            self.world.put(new_location, self)
            return Effect.EMPTY
        elif new_location_obj == CellType.WALL:
            return Effect.WALL
        else:
            return Effect.MEET_OTHER_BOT

    def eat(self, cell):
        if cell == CellType.FOOD:
            self.energy += 10
            return Effect.FOOD
        elif cell == CellType.POISON:
            return Effect.POISONED

    def peek(self, command):
        direction = get_direction_vector(self.direction.value[0], command)
        peek_location = self.location.transform(direction)
        if not is_in_range(peek_location):
            return
        peek_object = self.world.get(peek_location)
        if peek_object == CellType.FOOD:
            put_index = self.genes.put(command % 8)
            self.genes.move_pointer(put_index)
        elif peek_object == CellType.POISON:
            self.world.force_put(peek_location, CellType.FOOD)
            self.energy -= 1
            put_index = self.genes.put(command % 8)
            self.genes.move_pointer(put_index)

    def lookup(self, command):
        direction = get_direction_vector(self.direction.value[0], command)
        new_location = self.location.transform(direction)
        new_location_obj = self.world.get(new_location)
        if new_location_obj == CellType.FOOD:
            self.genes.put(command % 8)
        elif new_location_obj == CellType.POISON:
            self.genes.put(command % 8 + 8)
        else:
            self.genes.put(command % 8 + 24 + 1)

    def rotate(self, command):
        self.direction = get_direction(self.direction, command)

    def die(self):
        self.energy = 0
        self.bot_pool.bot_dead(self)
        if self.world.get(self.location) == self:
            self.world.force_put(self.location, CellType.EMPTY)

    # ---------------------------------------------------END STEP ------------------------------------------------------

    def __repr__(self):
        return str(self.energy)

    def __del__(self):
        self.energy = 0
        self.genes = []
