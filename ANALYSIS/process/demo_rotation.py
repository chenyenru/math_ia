import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sys

sys.path.insert(0, '/Users/chen_yenru/Documents/GitHub/SCHOOL/math_ia/ANALYSIS/modules')

import rotate
import custom_graph
import segment
import setup_data

x = np.arange(0, 20, 0.01)
# Amplitude of the sine wave is sine of a variable like time
y = np.sin(x)
xr, yr = rotate.rotate_matrix(x, y, angle=12)

max_x = np.arange(0, 20, 0.01)
max_y = np.ones(2000)
min_y = -(max_y)

max_xr, max_yr = rotate.rotate_matrix(max_x, max_y, angle=12)
min_xr, min_yr = rotate.rotate_matrix(max_x, min_y, angle=12)

fig = plt.figure(figsize=(12, 6))

plt.title("Time(s) vs. Lung Volume(L)")
plt.xlabel("Time (s)")
plt.ylabel("Lung Volume (L)")

plt.plot(x, y, label="Sine Wave y = sin(x)")
plt.plot(max_x, max_y, label="y=1", linestyle="dashed", color="#1f77b4")
plt.plot(max_x, min_y, label="y=-1", linestyle="dashed", color="#1f77b4")
plt.plot(xr, yr, label="y = sin(x) after counter-clockwise 12-degree rotation")
plt.plot(max_xr, max_yr, label="Maximum after counter-clockwise 12-degree rotation", linestyle="dashed", color="orange")
plt.plot(min_xr, min_yr, label="Maximum after counter-clockwise 12-degree rotation", linestyle="dashed", color="orange")
plt.legend()

plt.savefig('GRAPHS/demo_sin.svg')