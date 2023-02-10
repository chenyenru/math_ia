import pandas as pd
import numpy as np

import sys
sys.path.insert(0, '/Users/chen_yenru/Documents/GitHub/SCHOOL/math_ia/ANALYSIS/modules')

import rotate

segmented_run = pd.read_csv("DATA/Segmented_Data/segmented_run.csv")
print(segmented_run.columns)
segmented_run_X = segmented_run['Run 3: Time (s)']
segmented_run_Y = segmented_run['Run 3: Volume (L)']




sr_xr, sr_yr = rotate.negative_rotate_matrix(x=segmented_run_X,y=segmented_run_Y, angle=(theta), units="RADIAN")
srl_xr, srl_yr = rotate.negative_rotate_matrix(x=peak_x,y=predicted_peak_y, angle=(theta), units="RADIAN")
