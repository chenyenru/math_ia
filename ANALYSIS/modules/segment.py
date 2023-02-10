import numpy as np
import pandas as pd

import sys

def get_name(variable):
    return f'{variable=}'.split('=')[0]

def segmenting_in_plot(dataset, start_time = 30, time_length=180, run_count=1):
    vars(sys.modules[__name__])[f"{dataset}_segmented"] = dataset[
        (dataset[f'Run {run_count}: Time (s)'] < (start_time + time_length)) 
        & 
        (dataset[f'Run {run_count}: Time (s)'] > start_time)]

def segmenting(dataset, start_time = 30, time_length=180, run_count=1):
    return dataset[
        (dataset[f'Run {run_count}: Time (s)'] < (start_time + time_length)) 
        & 
        (dataset[f'Run {run_count}: Time (s)'] > start_time)]