from timeit import default_timer as time
import random
import sys
import threading
from main import BruteForceSolution
from main import BottomUpDynamicSolution
from main import TopDownDynamicSolution

number_of_test = 4
total_value = 5
brute_force_time = list()
bottom_up_dynamic_time = list()
top_down_dynamic_time = list()


class TimeCalculating:
    @staticmethod
    def time_calculating():
        given_list = [[[random.randint(1, 5) for i in range(1000 * (k + 1))] for j in range(total_value)] for k in
                      range(number_of_test)]
        for i in range(number_of_test):
            first_average_time = 0
            for j in range(total_value):
                start = time()
                brute_force = BruteForceSolution(given_list[i][j])
                brute_force.can_partition()
                interval = time() - start
                first_average_time += interval

            print(f"Time for brute force solution for {len(given_list[i][i])} numbers",
                  first_average_time / len(given_list[i]))

            brute_force_time.append(first_average_time / len(given_list[i]))

        for i in range(number_of_test):
            second_average_time = 0
            for j in range(total_value):
                start = time()
                top_down = TopDownDynamicSolution(given_list[i][j])
                top_down.can_partition()
                interval = time() - start
                second_average_time += interval

            print(f"Time for top down  solution for {len(given_list[i][i])} numbers",
                  second_average_time / len(given_list[i]))

            top_down_dynamic_time.append(second_average_time / len(given_list[i]))

        for i in range(number_of_test):
            third_average_time = 0
            for j in range(total_value):
                start = time()
                bottom_up = BottomUpDynamicSolution(given_list[i][j])
                bottom_up.can_partition()
                interval = time() - start
                third_average_time += interval

            print(f"Time for bottom up solution for {len(given_list[i][i])} numbers",
                  third_average_time / len(given_list[i]))

            bottom_up_dynamic_time.append(third_average_time / len(given_list[i]))


sys.setrecursionlimit(10 ** 8)
threading.stack_size(2 ** 26)
threading.Thread(target=TimeCalculating.time_calculating()).start()
