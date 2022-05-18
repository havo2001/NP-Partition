from timeit import default_timer as time
import random
import sys
import threading
from main import BruteForceSolution
from main import BottomUpDynamicSolution
from main import TopDownDynamicSolution

brute_force_time = list()


class TimeCalculating:
    @staticmethod
    def time_calculating():
        given_list = [[[random.randint(1, 5) for i in range(10 * (k + 1))] for j in range(5)] for k in range(4)]
        for i in range(4):
            average_time = 0
            for j in range(5):
                start = time()
                brute_force = BruteForceSolution(given_list[i][j])
                brute_force.can_partition()
                interval = time() - start
                average_time += interval
            print(f"Time for brute force solution for {len(given_list[i][i])} numbers",
                  average_time / len(given_list[i]))
            brute_force_time.append(average_time / len(given_list[i]))

        # second_time = 0
        # for i in range(5):
        #     start = time.time()
        #     top_down = TopDownDynamicSolution(self.given_list[i])
        #     top_down.can_partition()
        #     end = time.time()
        #     second_time += (end - start)
        # print("Time for top down dynamic solution:", second_time*1000/5)

        # third_time = 0
        # for i in range(5):
        #     start = time.time()
        #     bottom_up = BottomUpDynamicSolution(self.given_list[i])
        #     bottom_up.can_partition()
        #     end = time.time()
        #     third_time += (end - start)
        # print("Time for bottom up dynamic solution:", third_time*1000/5)


sys.setrecursionlimit(10 ** 8)
threading.stack_size(2 ** 26)
threading.Thread(target=TimeCalculating.time_calculating()).start()
