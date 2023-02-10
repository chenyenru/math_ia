import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from scipy import signal
from sklearn.linear_model import LinearRegression

import rotate
import setup

data = pd.read_csv("DATA/Segmented_Data/segmented_run.csv")

print(data)

