import numpy as np
import pandas as pd

list_1 = pd.read_csv("day_1_input_list_1.csv", header=None).to_numpy()
list_2 = pd.read_csv("day_1_input_list_2.csv", header=None).to_numpy()

list_1_sorted = np.sort(list_1)
list_2_sorted = np.sort(list_2)

diff = list_2_sorted - list_1_sorted
diff_sum = np.abs(diff).sum()

print(diff_sum)
