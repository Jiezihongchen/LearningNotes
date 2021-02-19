import numpy as np
import pandas as pd
import random
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from collections import defaultdict
import math


def load_data():
    path = "../ml-1m/ratings.dat"
    col_name = ['user_id', 'movie_id', 'rating', 'timestamp']
    ratings = pd.read_csv(
        path,
        sep="::",
        engine="python",
        header=None,
        names=col_name)

    train_df, test_df, _, _ = train_test_split(ratings, ratings, test_size=0.3)
    train_df = train_df.groupby(
        "user_id")["movie_id"].apply(list).reset_index()
    test_df = test_df.groupby("user_id")["movie_id"].apply(list).reset_index()

    train_df_dict = {}
    test_df_dict = {}
    # formation: {user_id1: (movie_id1, movie_id2……); user_id2:……}
    for user_id, movies in zip(train_df["user_id"], train_df["movie_id"]):
        train_df_dict[user_id] = set(movies)
    for user_id, movies in zip(test_df["user_id"], test_df["movie_id"]):
        test_df_dict[user_id] = set(movies)

    return train_df_dict, test_df_dict


def user_cf_rec(train_user_movies, test_user_movies, K=80, N=10):
    '''
    K: number of similar users
    N: number of recommended products
    '''
    # formation of inverted table: {movie_id1: (user_id1, user_id2……);
    # movie_id2:……}
    print("Create inverted table")
    inverted_table = defaultdict(set)
    for user_id, movie_set in tqdm(train_user_movies.items()):
        for movie in movie_set:
            inverted_table[movie].add(user_id)

    sim = defaultdict(dict)
    num = defaultdict(int)
    print("Create collaborative filtering matrix")
    for movie_id, user_id_set in tqdm(inverted_table.items()):
        for user_id in user_id_set:
            num[user_id] += 1
            for other_user_id in user_id_set:
                if other_user_id != user_id:
                    if other_user_id not in sim[user_id]:
                        sim[user_id][other_user_id] = 0
                    sim[user_id][other_user_id] += 1

    # use cos distance
    print("Calculate similarity")
    for user_id, other_user_sets in tqdm(sim.items()):
        for other_user_id, score in other_user_sets.items():
            sim[user_id][other_user_id] = score / \
                (math.sqrt(num[user_id] * num[other_user_id]))

    rank_movies = defaultdict(dict)
    print("Recommend to test users")
    for user_id, _ in tqdm(test_user_movies.items()):
        for other_user_id, score in sorted(
                sim[user_id].items(), key=lambda x: x[1], reverse=True)[
                0:K]:
            for movie_id in train_user_movies[other_user_id]:
                if movie_id not in rank_movies[user_id]:
                    rank_movies[user_id][movie_id] = 0
                rank_movies[user_id][movie_id] += score

    rank_movies = {
        key: sorted(
            value.items(),
            key=lambda x: x[1],
            reverse=True)[
            :K] for key,
        value in rank_movies.items()}
    rank_movies = {key: set([value[0] for item in value])
                   for key, value in rank_movies.items()}

    return rank_movies


def recall(rec_dict, val_dict):
    '''
    rec_dict: {user_id1: {movie_id1, ……}, user_id2……}
    val_dict: {user_id1: {movie_id1, ……}, user_id2……}
    '''
    hit_item = 0
    all_item = 0

    for user_id, movies in val_dict.items():
        rec_set = rec_dict[user_id]
        all_item += len(rec_set)
        for movie in movies:
            if movie in rec_set:
                hit_item += 1
    return round(hit_item / all_item * 100, 2)


def precision(rec_dict, val_dict):
    hit_item = 0
    all_item = 0

    for user_id, movies in rec_dict.items():
        true_set = val_dict[user_id]
        all_item += len(movies)
        for movie in movies:
            if movie in true_set:
                hit_item += 1
    return round(hit_item / all_item * 100, 2)


def rec_eval(rec_movies, test_user_movies):
    pass


if __name__ == "__main__":
    train_user_movies, test_user_movies = load_data()
    rec_movies = user_cf_rec(train_user_movies, test_user_movies)
