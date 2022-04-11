class BottomUpDynamicSolution:
    # Constructor receive a list of integer numbers
    def __init__(self, given_list):
        self.given_list = given_list

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

