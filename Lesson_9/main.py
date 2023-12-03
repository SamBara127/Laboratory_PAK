
import pandas as pd
import sklearn.metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression


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


if __name__ == "__main__":
    tab = pd.read_csv('titanic_prepared.csv', index_col=0, delimiter=',')
    # делаем сплит датасета на тестовую и обучающую выборку
    x_train, x_test, y_train, y_test = get_train_and_test(tab)

    _, acc1 = decision_tree(y_test, x_test, y_train, x_train)
    _, acc2 = xgboost(y_test, x_test, y_train, x_train)
    _, acc3 = logistic_regression(y_test, x_test, y_train, x_train)
    _, acc4 = most_important(y_test, x_test, y_train, x_train, 2)