from abc import ABC
import sys
import time


sys.setrecursionlimit(15000)


class Partition(ABC):
    def __init__(self, given_list):
        self.given_list = given_list

    def can_partition(self):
        pass


class BruteForceSolution(Partition):
    def can_partition(self):
        # First calculate the sum of all elements, if it is odd then we can't partition
        total = sum(self.given_list)
        if total % 2 != 0:
            return False

        # If the sum is even then we need to check recursion partition
        else:
            return self.recursion_partition(self.given_list, total / 2, 0)

    def recursion_partition(self, given_list, total, index):
        # Base check, if total is equal zero then we can partition
        if total == 0:
            return True

        size = len(given_list)
        # If we visit all elements and the total sum is not zero then return False
        if size == 0 or index >= size:
            return False

        # First we check number "index", if the number "index" doesn't exceed sum, the sum of list, we may include this
        # number by decreasing the sum by exact number "index", and continue check with "index + 1"
        if given_list[index] <= total:
            if self.recursion_partition(given_list, total - given_list[index], index + 1):
                return True

        # Recursive call after excluding number "index"
        return self.recursion_partition(given_list, total, index + 1)


class BottomUpDynamicSolution(Partition):
    def can_partition(self):
        # First calculate the sum of all elements, if it is odd then we can't partition
        total = sum(self.given_list)
        if total % 2 != 0:
            return False

        # If the sum is even then we need to check recursion partition
        total = int(total / 2)
        size = len(self.given_list)
        dp = [[False for i in range(total + 1)] for j in range(size)]

        # dp[i][j] when i is the index of element in the list and j is the sum
        # when j = 0 then the value of dp[i][0] = True because we don't need to
        # add any elements
        for i in range(0, size):
            dp[i][0] = True

        # With only one number, we can form a subset only when the required sum
        # equal to its value
        for j in range(1, total + 1):
            dp[0][j] = (self.given_list[0] == j)

        # process all subsets for all sums
        for i in range(1, size):
            for j in range(1, total + 1):
                # if we can get the sum 'j' without the number at index 'i'
                if dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                elif j >= self.given_list[i]:
                    # we can find a subset to get the remaining sum
                    dp[i][j] = dp[i - 1][j - self.given_list[i]]

        return dp[size - 1][total]


class TopDownDynamicSolution(Partition):
    def can_partition(self):
        # First calculate the sum of all elements, if it is odd then we can't partition
        total = sum(self.given_list)

        if total % 2 != 0:
            return False
        else:
            dp = [[False for i in range(int(total/2)+1)] for j in range(len(self.given_list))]
            if self.recursion_partition(dp, self.given_list, int(total/2), 0):
                return True
            else:
                return False

    def recursion_partition(self, dp, given_list, total, index):
        # Base check, if total is equal zero then we can partition
        if total == 0:
            return True

        size = len(given_list)
        # If we visit all elements and the total sum is not zero then return False
        if size == 0 or index >= size:
            return False

        # If we haven't already processed this problem
        if not dp[index][total]:
            # Recursively call after choosing the number at index, and it doesn't
            # exceed the sum we process it
            if given_list[index] <= total:
                if self.recursion_partition(dp, given_list, total - given_list[index], index + 1):
                    dp[index][total] = True
                    return True
            # If the number exceeds the sum, we exclude it, and work with index + 1
            dp[index][total] = self.recursion_partition(dp, given_list, total, index + 1)

        return dp[index][total]


class TimeCalculating:
    def __init__(self, giv_list):
        self.given_list = giv_list

    def time_calculating(self):

        first_time = 0
        start = time.time()
        brute_force = BruteForceSolution(self.given_list)
        brute_force.can_partition()
        end = time.time()
        first_time += (end - start)
        print("Time for brute force solution:", first_time)

        second_time = 0
        start = time.time()
        top_down = TopDownDynamicSolution(self.given_list)
        top_down.can_partition()
        end = time.time()
        second_time += (end - start)
        print("Time for top down dynamic solution:", second_time)

        third_time = 0
        start = time.time()
        bottom_up = BottomUpDynamicSolution(self.given_list)
        bottom_up.can_partition()
        end = time.time()
        third_time += (end - start)
        print("Time for bottom up dynamic solution:", third_time)

