from random import randint

from src.const.config import MAX_GENES_COUNT, HIGHEST_GENE


class Genes:
    def __init__(self):
        self.genes = rand_genes()
        self.genes_pointer = 0
        self.last_index = len(self.genes) - 1

    def put(self, gene):
        self.genes.insert(self.genes_pointer, gene)
        self.genes_pointer += 1
        if self.genes_pointer >= MAX_GENES_COUNT:
            self.genes_pointer = 0
        if self.last_index < MAX_GENES_COUNT - 1:
            self.last_index += 1
        return self.genes_pointer

    def get_next(self):
        return self.genes[self.genes_pointer]

    def mutate(self):
        stop = randint(0, 5)
        mutated_indexes = set()
        while stop > 0:

            i = randint(0, self.last_index)
            while i in mutated_indexes:
                i = randint(0, self.last_index)

            new_gen = randint(0, HIGHEST_GENE)
            while self.genes[i] == new_gen:
                new_gen = randint(0, HIGHEST_GENE)

            self.genes[i] = new_gen
            mutated_indexes.add(i)
            stop -= 1

    def shift_pointer(self, cells):
        self.genes_pointer += cells
        if self.genes_pointer > self.last_index:
            self.genes_pointer %= self.last_index

    def move_pointer(self, index):
        self.genes_pointer = index
        if self.genes_pointer > self.last_index:
            self.genes_pointer %= self.last_index

    def __repr__(self):
        acc = ""
        for i in range(0, self.genes_pointer):
            acc += str(self.genes[i]) + " "
            if i % 8 == 0:
                acc += "\n"
        return acc


def rand_genes():
    genes = []
    for i in range(0, 12):
        genes.insert(i, randint(0, 7))
    return genes
