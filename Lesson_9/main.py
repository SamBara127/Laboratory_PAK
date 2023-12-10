
import pandas as pd
import sklearn.metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.base import BaseEstimator
from sklearn.utils import shuffle
import numpy as np


def get_train_and_test(df):
    df_l = df.pop('label')
    # df - обучающая выборка или train_set; df_l - тестовая выборка или test_set 
    return train_test_split(df, df_l, test_size=0.1)


def decision_tree(y_test, x_test, y_train, x_train):
    cl = DecisionTreeClassifier()
    cl.fit(x_train, y_train)
    res = cl.predict(x_test)
    acc = sklearn.metrics.accuracy_score(y_test, res)
    return res, acc


def xgboost(y_test, x_test, y_train, x_train):
    clfr = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
    clfr.fit(x_train, y_train)
    res = clfr.predict(x_test)
    acc = sklearn.metrics.accuracy_score(y_test, res)
    return res, acc


def logistic_regression(y_test, x_test, y_train, x_train):
    cl = LogisticRegression(solver='liblinear', random_state=0)
    cl.fit(x_train, y_train)
    res = cl.predict(x_test)
    acc = sklearn.metrics.accuracy_score(y_test, res)
    return res, acc


def most_important(y_test, x_test, y_train, x_train, amount_of_properties):
    cl = DecisionTreeClassifier()
    cl.fit(x_train, y_train)
    f = cl.feature_importances_
    f = f[-amount_of_properties:]
    most_important_features = x_train.iloc[:, f]
    test_important_features = x_test.iloc[:, f]
    cl = DecisionTreeClassifier()
    cl.fit(most_important_features, y_train)
    res = cl.predict(test_important_features)
    acc = sklearn.metrics.accuracy_score(y_test, res)
    return res, acc



class MyRandomForest(BaseEstimator):
    # для построения слуаяного леса будем использовать так называемых "отдельных оценщиков" 
    # из класса BaseEstimator. Каждому мы отдадим 
    def __init__(self, n_estimators=50, max_depth=None, random_state=None):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.random_state = random_state
        self.estimators = []

    def fit(self, X, y):
        np.random.seed(self.random_state)
        self.estimators = []

        X_bootstrap = np.array_split(X, self.n_estimators)
        y_bootstrap = np.array_split(y, self.n_estimators)

        for i in range(self.n_estimators):
            # Bootstrap sampling
            # indices = np.random.choice(X.shape[0], X.shape[0], replace=True)
            # X_bootstrap = X[indices]
            # y_bootstrap = y[indices]

            # Create and train a decision tree
            tree = DecisionTreeClassifier(max_depth=self.max_depth, random_state=self.random_state)
            tree.fit(X_bootstrap[i], y_bootstrap[i])

            # Save the trained tree
            self.estimators.append(tree)

    def predict(self, X):
        # Aggregate predictions from all trees
        predictions = np.array([tree.predict(X) for tree in self.estimators])
        # Use majority voting to get the final prediction
        final_predictions = np.apply_along_axis(lambda x: np.bincount(x).argmax(), axis=0, arr=predictions)
        return final_predictions
    


if __name__ == "__main__":
    tab = pd.read_csv('titanic_prepared.csv', index_col=0, delimiter=',')
    # делаем сплит датасета на тестовую и обучающую выборку
    x_train, x_test, y_train, y_test = get_train_and_test(tab)

    _, acc1 = decision_tree(y_test, x_test, y_train, x_train)
    _, acc2 = xgboost(y_test, x_test, y_train, x_train)
    _, acc3 = logistic_regression(y_test, x_test, y_train, x_train)
    _, acc4 = most_important(y_test, x_test, y_train, x_train, 2)

    print(acc1)
    print(acc2)
    print(acc3)
    print(acc4)

    # Создание и обучение MyRandomForest
    my_rf = MyRandomForest()
    # for i in range(10):
    
    # print(x_train)        
    # indices = np.random.choice(x_train.shape[0], x_train.shape[0], replace=True)
    # print(x_train.iloc[indices])
    # print(shuffle(x_train))
    # print('SPLITTER')
    # num_splits = 100
    # x_train_splits = np.array_split(x_train, num_splits)
    # y_train_splits = np.array_split(y_train, num_splits)
    # print(x_train_splits[0])
    # print(y_train_splits[0])

    my_rf.fit(x_train, y_train)

    # Прогнозирование
    y_pred = my_rf.predict(x_test)

    # Оценка точности
    accuracy = sklearn.metrics.accuracy_score(y_test, y_pred)
    # print(f'Accuracy: {accuracy:.2f}')
    print(f'Accuracy: {accuracy}')