import numpy as np
import random
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model

# 生成训练数据，y=2x+随机数
x_train = np.linspace(0, 10, 100)
y_train_random = -1 + 2 * np.random.random(100)
y_train = 2 * x_train + y_train_random
print("x_train \n", x_train)
print("y_train \n", y_train)

# 生成测试数据
x_test = np.linspace(0, 10, 100)
y_test_random = -1 + 2 * np.random.random(100)
y_test = 2 * x_test + y_test_random
print("x_test \n", x_test)
print("y_test \n", y_test)

# 预测数据
x_predict = random.sample(range(0, 10), 10)

# 定义网络层1个输入层，3个全连接层
inputs = Input(shape=(1,))
x = Dense(64, activation='relu')(inputs)
x = Dense(64, activation='relu')(x)
predictions = Dense(1)(x)

# 编译模型，指定训练参数
model = Model(inputs=inputs, outputs=predictions)
model.compile(optimizer='rmsprop',
              loss='mse',
              metrics=['mae'])

# 训练模型，指定训练的超参数
history = model.fit(x_train,
                    y_train,
                    epochs=100,
                    batch_size=16)

# 测试模型
score = model.evaluate(x_test,
                       y_test,
                       batch_size=16)
print("score \n", score)
y_predict = model.predict(x_predict)
print("x_predict \n", x_predict)
print("y_predict \n", y_predict)