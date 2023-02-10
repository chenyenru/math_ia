import pandas as pd

quiet = pd.read_csv("DATA/Original_Data/spiro-quiet.csv")
deep = pd.read_csv("DATA/Original_Data/spiro-deep.csv")
run = pd.read_csv("DATA/Original_Data/spiro-run.csv")

# Setting up the dataset
dataset = [quiet, deep, run]
dataset_names = ["quiet", "deep", "run"]

# dataset.to_csv("DATA/Segmented_Data/segmented_data.csv")