from random import randint

from src.const.config import MAX_GENES_COUNT, MAX_MUTATION_GENES, HIGHEST_GENE


class Genes:

    def __init__(self):
        self.genes = rand_genes()
        self.pointer = 0
        self.last_index = len(self.genes) - 1

    def get_next(self):
        next_gene = self.genes[self.pointer]
        self.shift_pointer(1)
        return next_gene

    def shift_pointer(self, shift_index):
        self.pointer = (shift_index + self.pointer) % (self.last_index + 1)

    def move_pointer(self, move_index):
        self.pointer = move_index % (self.last_index + 1)

    def mutate(self):
        stop = randint(0, self.last_index // 3)
        if stop > MAX_MUTATION_GENES:
            stop = MAX_MUTATION_GENES
        mutated_indexes = set()
        while stop > 0:
            stop -= 1
            index = randint(0, self.last_index)
            while index in mutated_indexes:
                index = randint(0, self.last_index)
            new_gen = randint(0, 32)
            while self.genes[index] == new_gen:
                new_gen = randint(0, 32)
            self.genes[index] = new_gen
            mutated_indexes.add(index)
        return self

    def clone(self):
        clone = Genes()
        clone.pointer = 0
        clone.last_index = self.last_index
        clone.genes = self.genes.copy()
        return clone

    def __len__(self):
        return len(self.genes)


def rand_genes():
    genes = []
    for i in range(0, MAX_GENES_COUNT):
        gene = randint(0, HIGHEST_GENE)
        genes.append(gene)
    return genes
