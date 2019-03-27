import unittest

import numpy as np

from src.bot.genes import Genes
from src.const.config import MAX_GENES_COUNT


class GenesTest(unittest.TestCase):

    def test_init(self):
        genes = Genes()
        self.assertEqual(10, len(genes))
        self.assertEqual(0, genes.pointer)
        self.assertEqual(9, genes.last_index)

    def test_get_next(self):
        genes = Genes()
        gene = genes.get_next()
        self.assertIn(gene, range(0, 33))

    def test_put(self):
        genes = Genes()
        genes.put(18)
        self.assertEqual(11, len(genes))
        self.assertEqual(10, genes.last_index)
        self.assertEqual(0, genes.pointer)
        self.assertEqual(18, genes.genes[10])

    def test_put_with_shift(self):
        pass

    def test_shift_pointer(self):
        genes = Genes()
        genes.genes = np.arange(0, 64)
        genes.pointer = 64
        genes.last_index = 64
        genes.put_index = 0
        genes.put_with_point(1)
        self.assertEqual(0, genes.pointer)
        self.assertEqual(64, genes.last_index)
        self.assertEqual(0, genes.put_index)

    def test_shift_pointer_no_cycle(self):
        genes = Genes()
        self.assertEqual(0, genes.pointer)
        genes.shift_pointer(1)
        self.assertEqual(1, genes.pointer)

    def test_shift_pointer_cycle(self):
        genes = Genes()
        self.assertEqual(0, genes.pointer)
        genes.shift_pointer(10)
        self.assertEqual(0, genes.pointer)

    def test_shift_pointer_cycle_2(self):
        genes = Genes()
        self.assertEqual(0, genes.pointer)
        genes.shift_pointer(15)
        self.assertEqual(5, genes.pointer)

    def test_shift_pointer_cycle_3(self):
        genes = Genes()
        genes.put(1)
        self.assertEqual(0, genes.pointer)
        genes.shift_pointer(15)
        self.assertEqual(4, genes.pointer)

    def test_shift_pointer_cycle_4(self):
        genes = Genes()
        self.assertEqual(0, genes.pointer)
        genes.shift_pointer(1)
        self.assertEqual(1, genes.pointer)
        genes.shift_pointer(1)
        self.assertEqual(2, genes.pointer)

    def test_shift_pointer_cycle_5(self):
        genes = Genes()
        self.assertEqual(0, genes.pointer)
        genes.shift_pointer(1)
        self.assertEqual(1, genes.pointer)
        genes.shift_pointer(10)
        self.assertEqual(1, genes.pointer)

    def test_move_index_no_cycle(self):
        genes = Genes()
        self.assertEqual(0, genes.pointer)
        genes.move_pointer(5)
        self.assertEqual(5, genes.pointer)

    def test_move_index_cycle(self):
        genes = Genes()
        self.assertEqual(0, genes.pointer)
        genes.move_pointer(10)
        self.assertEqual(0, genes.pointer)

    def test_move_index_cycle_2(self):
        genes = Genes()
        self.assertEqual(0, genes.pointer)
        genes.move_pointer(15)
        self.assertEqual(5, genes.pointer)

    def test_move_index_cycle_3(self):
        genes = Genes()
        self.assertEqual(0, genes.pointer)
        genes.put(1)
        genes.move_pointer(1)
        self.assertEqual(1, genes.pointer)

    def test_put_with_point(self):
        genes = Genes()
        genes.put_with_point(65)
        self.assertEqual(10, genes.pointer)
        self.assertEqual(65, genes.get_next())
        self.assertEqual(11, genes.put_index)

    def test_mutate(self):
        genes = Genes()
        genes.put_with_point(65)
        self.assertEqual(len(genes), 11)
        genes.mutate()
        self.assertEqual(len(genes), 11)


if __name__ == '__main__':
    unittest.main()
