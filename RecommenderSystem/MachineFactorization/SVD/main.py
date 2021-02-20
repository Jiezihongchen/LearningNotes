from surprise import Dataset
from surprise import SVD
from surprise import accuracy
from surprise.model_selection import train_test_split, cross_validate

if __name__ == "__main__":
    data_df = Dataset.load_builtin("ml-100k")
    # train_set的类型是surprise.dataset.Trainset类型
    # train_df.n_users: 943
    # train_df.n_items: 1627
    train_df, test_df = train_test_split(data_df, test_size=0.3)

    svd_model = SVD(n_factors=35)
    #cross_validate(svd_model, data_df, measures=["RMSE", "MAE"], cv=5, verbose=True)
    svd_model.fit(train_df)

    y_pred = svd_model.test(test_df)
    accuracy.rmse(y_pred)

    # recommendation
    user_id = str(196)
    item_id = str(302)
    y_pred = svd_model.predict(user_id, item_id, r_ui=4, verbose=True)
