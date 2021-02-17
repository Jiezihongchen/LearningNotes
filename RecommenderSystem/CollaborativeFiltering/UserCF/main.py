import numpy as np
import pandas as pd
import random
from tqdm import tqdm
from sklearn.model_selection import train_test_split


def load_data():
    path = "../ml-1m/ratings.dat"
    col_name = ['user_id', 'movie_id', 'rating', 'timestamp']
    ratings = pd.read_csv(
        path,
        sep="::",
        engine="python",
        header=None,
        names=col_name)


if __name__ == "__main__":
    load_data()
