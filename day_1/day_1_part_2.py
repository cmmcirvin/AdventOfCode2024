import numpy as np
import pandas as pd

list_1 = pd.read_csv("day_1_input_list_1.csv", header=None).to_numpy().flatten()
list_2 = pd.read_csv("day_1_input_list_2.csv", header=None).to_numpy().flatten()

similarity_score = 0
list_2_counts = {}

for element in list_2:
    if element in list_2_counts:
        list_2_counts[element] += 1
    else:
        list_2_counts[element] = 1

for element in list_1:
    similarity_score += element * list_2_counts.get(element, 0)

print(similarity_score)
