from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, RidgeCV
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib


def dump_load_demo():
    """
    '模型的保存和加载
    :return:
    """
    boston = load_boston()
    x_train, x_test, y_train, y_test = train_test_split(boston.data, boston.target, random_state=22, test_size=0.2)
    # 3.特征工程 --标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)
    estimator = joblib.load("./data/test.pkl")
    y_pre = estimator.predict(x_test)
    print("预测值是:\n", y_pre)
    score = estimator.score(x_test, y_test)
    print("准确率是:\n", score)
    ret = mean_squared_error(y_test, y_pre)
    print("均方误差是:\n", ret)


if __name__ == '__main__':
    dump_load_demo()
