import matplotlib.pyplot as graph
from benchmark import brute_force_time
from benchmark import top_down_dynamic_time
from benchmark import bottom_up_dynamic_time


size = [1000*(i + 1) for i in range(4)]
graph.plot(size, brute_force_time, label="Brute Force Solution")
graph.plot(size, top_down_dynamic_time, label="Top Down Dynamic Solution")
graph.plot(size, bottom_up_dynamic_time, label="Bottom Up Dynamic Solution")
graph.legend()
graph.show()
