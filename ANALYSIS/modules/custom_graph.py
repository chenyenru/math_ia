import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import sys
def plot(dataset, run_count, names=["quiet", "deep", "Spirometry Run"], size=0.5):
    # plt.figure(run_count)
    # Plot 1

    plt.subplot(211)
    plt.title("Time(s) vs. Lung Volume(L)")
    plt.xlabel("Time (s)")
    plt.ylabel("Lung Volume (L)")
    plt.scatter(
        dataset[f'Run {run_count}: Time (s)'], 
        dataset[f'Run {run_count}: Volume (L)'], 
        label=names[run_count-1],
        s=size)
    # # Plot 2
    # plt.subplot(212)
    # plt.title("Volume(L) vs. Flow Rate (L/s)")
    # plt.xlabel("Volume (L)")
    # plt.ylabel("Flow Rate (L/s)")
    # plt.plot(dataset[f'Run {run_count}: Volume (L)'], dataset[f"Run {run_count}: Flow Rate (L/s)"], label=names[run_count-1])

    plt.legend()
