import random
import unittest
from sorting import bubble_sort, quick_sort, partition


class SortingTests(unittest.TestCase):
    def test_examples(self):
        examples = [[], [1], [1, 2, 3], [3, 2, 1], [2, 2, 2],
                    [-3, 0, 7, -1, 7], [1, 4, 8, 6, 7, 42, 2, 2, 8, 100, 3, 5]]
        for sort in [bubble_sort, quick_sort]:
            for values in examples:
                with self.subTest(sort=sort.__name__, values=values):
                    arr = values.copy()
                    self.assertIs(sort(arr), arr)
                    self.assertEqual(arr, sorted(values))

    def test_random_lists(self):
        rng = random.Random(42)
        for _ in range(100):
            values = [rng.randint(-100, 100) for _ in range(rng.randrange(80))]
            for sort in [bubble_sort, quick_sort]:
                self.assertEqual(sort(values.copy()), sorted(values))

    def test_lomuto_partition(self):
        arr = [9, 4, 1, 7, 3, 8]
        original = arr.copy()
        index = partition(arr, 1, 4)
        self.assertEqual(arr[index], 3)
        self.assertTrue(all(x <= 3 for x in arr[1:index]))
        self.assertTrue(all(x > 3 for x in arr[index + 1:5]))
        self.assertEqual(arr[0], original[0])
        self.assertEqual(arr[-1], original[-1])
        self.assertCountEqual(arr, original)

    def test_quick_sort_long_sorted_input(self):
        values = list(range(1500))
        self.assertEqual(quick_sort(values.copy()), values)
        self.assertEqual(quick_sort(values[::-1]), values)


if __name__ == '__main__':
    unittest.main()
