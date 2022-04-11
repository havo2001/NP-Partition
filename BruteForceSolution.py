class BruteForceSolution:
    # Constructor receive a list of integer numbers
    def __init__(self, given_list):
        self.given_list = given_list

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
