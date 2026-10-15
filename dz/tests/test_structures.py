import random
import unittest
from collections import deque

from my_array import Array
from linked_list import LinkedList
from my_deque import Deque
from avl_tree import AVLTree


class ArrayTests(unittest.TestCase):
    def test_operations(self):
        arr = Array(3)
        for value in [10, 20, 30]:
            arr.append(value)
        self.assertEqual(arr.get(1), 20)
        arr.set(1, 25)
        self.assertEqual(arr.find(25), 1)
        self.assertEqual(arr.find(99), -1)
        self.assertEqual(arr.delete(0), 10)
        self.assertEqual(arr.to_list(), [25, 30])
        arr.append(40)
        self.assertEqual(arr.to_list(), [25, 30, 40])
        self.assertEqual(len(arr), 3)

    def test_limits(self):
        with self.assertRaises(ValueError):
            Array(-1)
        with self.assertRaises(OverflowError):
            Array(0).append(1)
        arr = Array(1)
        arr.append(7)
        with self.assertRaises(OverflowError):
            arr.append(8)
        for index in [-1, 1]:
            with self.assertRaises(IndexError):
                arr.get(index)
            with self.assertRaises(IndexError):
                arr.set(index, 0)
            with self.assertRaises(IndexError):
                arr.delete(index)
        self.assertEqual(arr.delete(0), 7)
        self.assertEqual(arr.to_list(), [])
        self.assertEqual(len(arr), 0)


class ListTests(unittest.TestCase):
    def test_add_and_find(self):
        items = LinkedList()
        self.assertEqual(items.to_list(), [])
        self.assertEqual(items.find(5), -1)
        items.append(2)
        items.prepend(1)
        items.append(3)
        self.assertEqual(items.to_list(), [1, 2, 3])
        self.assertEqual(items.find(2), 1)
        self.assertEqual(len(items), 3)

    def test_delete(self):
        items = LinkedList()
        self.assertFalse(items.delete(7))
        for value in [1, 2, 2, 3]:
            items.append(value)
        self.assertTrue(items.delete(2))
        self.assertEqual(items.to_list(), [1, 2, 3])
        for value in [1, 3, 2]:
            self.assertTrue(items.delete(value))
        self.assertEqual(items.to_list(), [])
        self.assertEqual(len(items), 0)
        items.prepend(9)
        self.assertEqual(items.to_list(), [9])


class DequeTests(unittest.TestCase):
    def test_empty_and_reuse(self):
        items = Deque()
        for remove in [items.pop, items.pop_left]:
            with self.assertRaises(IndexError):
                remove()
        items.append(1)
        self.assertEqual(items.pop_left(), 1)
        items.append_left(2)
        self.assertEqual(items.pop(), 2)
        self.assertIsNone(items.head)
        self.assertIsNone(items.tail)
        self.assertEqual(len(items), 0)

    def test_delete(self):
        items = Deque()
        for value in [1, 2, 2, 3]:
            items.append(value)
        self.assertTrue(items.delete(2))
        self.assertEqual(items.to_list(), [1, 2, 3])
        self.assertFalse(items.delete(8))
        for value in [1, 3, 2]:
            self.assertTrue(items.delete(value))
        self.assertEqual(len(items), 0)
        self.assertIsNone(items.head)
        self.assertIsNone(items.tail)

    def test_random_operations(self):
        rng = random.Random(16)
        items = Deque()
        expected = deque()
        for _ in range(500):
            operation = rng.randrange(5)
            value = rng.randrange(20)
            if operation == 0:
                items.append(value)
                expected.append(value)
            elif operation == 1:
                items.append_left(value)
                expected.appendleft(value)
            elif operation == 2 and expected:
                self.assertEqual(items.pop(), expected.pop())
            elif operation == 3 and expected:
                self.assertEqual(items.pop_left(), expected.popleft())
            elif operation == 4:
                found = value in expected
                self.assertEqual(items.delete(value), found)
                if found:
                    expected.remove(value)
            self.assertEqual(items.to_list(), list(expected))
            self.assertEqual(len(items), len(expected))
            reverse = []
            current = items.tail
            while current is not None:
                reverse.append(current.value)
                current = current.prev
            self.assertEqual(reverse, list(reversed(expected)))


class AVLTests(unittest.TestCase):
    def check_tree(self, tree, expected):
        self.assertEqual(tree.to_list(), sorted(expected))

        def check(node, lower, upper):
            if node is None:
                return 0
            self.assertLess(lower, node.value)
            self.assertLess(node.value, upper)
            left = check(node.left, lower, node.value)
            right = check(node.right, node.value, upper)
            self.assertLessEqual(abs(left - right), 1)
            self.assertEqual(node.height, 1 + max(left, right))
            return node.height

        check(tree.root, float('-inf'), float('inf'))

    def test_four_rotations(self):
        for values in [[3, 2, 1], [1, 2, 3], [3, 1, 2], [1, 3, 2]]:
            with self.subTest(values=values):
                tree = AVLTree()
                for value in values:
                    tree.insert(value)
                self.assertEqual(tree.root.value, 2)
                self.check_tree(tree, values)

    def test_find_duplicates_and_missing(self):
        tree = AVLTree()
        self.assertFalse(tree.find(5))
        tree.delete(5)
        tree.insert(5)
        tree.insert(5)
        self.assertTrue(tree.find(5))
        self.assertFalse(tree.find(6))
        tree.delete(6)
        self.check_tree(tree, [5])
        tree.delete(5)
        self.check_tree(tree, [])

    def test_insert_and_delete_balance(self):
        rng = random.Random(16)
        values = list(range(150))
        rng.shuffle(values)
        tree = AVLTree()
        expected = set()
        for value in values:
            tree.insert(value)
            expected.add(value)
            self.check_tree(tree, expected)
        rng.shuffle(values)
        for value in values:
            tree.delete(value)
            expected.remove(value)
            self.assertFalse(tree.find(value))
            self.check_tree(tree, expected)


if __name__ == '__main__':
    unittest.main()
