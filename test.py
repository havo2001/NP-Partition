import unittest
import random

from main import BruteForceSolution
from main import BottomUpDynamicSolution
from main import TopDownDynamicSolution


class Test(unittest.TestCase):
    def test_case1(self):
        random_list = [random.randint(1, 100) for i in range(1000)]
        brute_force = BruteForceSolution(random_list)
        top_down = TopDownDynamicSolution(random_list)
        bottom_up = BottomUpDynamicSolution(random_list)
        self.assertEqual(brute_force.can_partition(), top_down.can_partition(), bottom_up.can_partition())

    def test_case2(self):
        random_list = [i for i in range(1000)]
        brute_force = BruteForceSolution(random_list)
        top_down = TopDownDynamicSolution(random_list)
        bottom_up = BottomUpDynamicSolution(random_list)
        self.assertEqual(brute_force.can_partition(), True)
        self.assertEqual(top_down.can_partition(), True)
        self.assertEqual(bottom_up.can_partition(), True)

    def test_case3(self):
        random_list = [1 for i in range(1000)]
        brute_force = BruteForceSolution(random_list)
        top_down = TopDownDynamicSolution(random_list)
        bottom_up = BottomUpDynamicSolution(random_list)
        self.assertEqual(brute_force.can_partition(), True)
        self.assertEqual(top_down.can_partition(), True)
        self.assertEqual(bottom_up.can_partition(), True)

    def test_case4(self):
        random_list = [1, 5, 6, 3, 3]
        brute_force = BruteForceSolution(random_list)
        top_down = TopDownDynamicSolution(random_list)
        bottom_up = BottomUpDynamicSolution(random_list)
        self.assertEqual(brute_force.can_partition(), True)
        self.assertEqual(top_down.can_partition(), True)
        self.assertEqual(bottom_up.can_partition(), True)

