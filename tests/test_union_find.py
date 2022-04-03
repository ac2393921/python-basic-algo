import os, sys, unittest

from tree.union_find import UnionFind


class TestUnionFind(unittest.TestCase):
    """test class of union_find.py
    """

    def setUp(self):
        if sys.flags.debug: print(os.linesep + "> setUp method is called.")
        self.n = 7
        self.uf = UnionFind(self.n)
        self.data = [[1, 3], [2, 4], [2,6]]
        self.parents = [-1, -2, -3, 1, 2, -1, 2]
        self.x = 3
        self.y = 2

    def test_find(self):
        expected = 1
        self.uf.parents = self.parents
        actual = self.uf.find(self.x)

        self.assertEqual(expected, actual)

    def test_union(self):
        expected = [-1, -1, -2, -1, 2, -1, -1]
        self.uf.union(2, 4)
        actual = self.uf.parents

        self.assertEqual(expected, actual)

    def test_size(self):
        expected = 3
        self.uf.parents = self.parents
        actual = self.uf.size(4)

        self.assertEqual(expected, actual)

    def test_same_true(self):
        self.uf.parents = self.parents
        actual = self.uf.same(4, 6)

        self.assertTrue(actual)

    def test_same_false(self):
        self.uf.parents = self.parents
        actual = self.uf.same(1, 6)

        self.assertFalse(actual)

    def test_members(self):
        expected = [1, 3]
        self.uf.parents = self.parents
        actual = self.uf.members(1)

        self.assertEqual(expected, actual)

    def test_roots(self):
        expected = [0, 1, 2, 5]
        self.uf.parents = self.parents
        actual = self.uf.roots()

        self.assertEqual(expected, actual)

    def test_group_count(self):
        expected = 4
        self.uf.parents = self.parents
        actual = self.uf.group_count()

        self.assertEqual(expected, actual)

    def test_all_group_members(self):
        expected = {0: [0], 1: [1, 3], 2: [2, 4, 6], 5: [5]}
        self.uf.parents = self.parents
        actual = self.uf.all_group_members()

        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()