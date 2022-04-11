class TopDownDynamicSolution:
    # Constructor receive a list of integer numbers
    def __init__(self, given_list):
        self.given_list = given_list

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
            # Recursively call after choosing the number at index and if doesn't
            # exceed the sum we process it
            if given_list[index] <= total:
                if self.recursion_partition(dp, given_list, total - given_list[index], index + 1):
                    dp[index][total] = True
                    return True
            # If the number exceeds the sum, we exclude it, and work with index + 1
            dp[index][total] = self.recursion_partition(dp, given_list, total, index + 1)

        return dp[index][total]
