import matplotlib.pyplot as graph
from benchmark import brute_force_time


size = [500, 1000, 1500, 2000]
# time1 = [0.2, 0.2, 0.4, 0.4, 0.4, 0.4, 0.6, 0.6]
# time2 = [4.1, 20.1, 64.8, 118.4, 124.4, 169.3, 235.7, 455.1]
# time3 = [24.7, 115.1, 387.7, 687.9, 719.3, 1076.7, 1431.5, 2866.1]
graph.plot(size, brute_force_time, label="Brute Force Solution")
# graph.plot(size, time2, label="Top Down Dynamic Solution")
# graph.plot(size, time3, label="Bottom Up Dynamic Solution")
graph.legend()
graph.show()
