from BruteForceSolution import BruteForceSolution
from TopDownDynamicSolution import TopDownDynamicSolution
from BottomUpDynamicSolution import BottomUpDynamicSolution

brute_force = BruteForceSolution([3, 1, 1, 1, 100])
top_down = TopDownDynamicSolution([3, 1, 1, 1, 100])
bottom_up = BottomUpDynamicSolution([3, 1, 1, 1, 100])
print(brute_force.can_partition())
print(top_down.can_partition())
print(bottom_up.can_partition())
