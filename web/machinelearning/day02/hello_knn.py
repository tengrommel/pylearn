# coding:utf-8
from sklearn.neighbors import KNeighborsClassifier

# 获取数据
x = [[1], [2], [0], [0]]
y = [1, 1, 0, 0]
# 机器学习
# 1、实例化一个训练模型
estimator = KNeighborsClassifier(n_neighbors=2)
# 2、调用fit方法进行训练
estimator.fit(x, y)

# 预测其他值
ret = estimator.predict([[-1]])
print(ret)
