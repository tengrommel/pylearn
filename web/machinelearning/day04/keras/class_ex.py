import tensorflow as tf
import tensorflow.keras
import numpy as np
from tensorflow.keras.layers import Dense, Input, Layer
from tensorflow.keras.models import Model
import random


class MyLayer(Layer):
    # 自定义一个类，继承自Layer
    def __init__(self, output_dim, **kwargs):
        self.output_dim = output_dim
        super(MyLayer, self).__init__(**kwargs)

    # 定义build方法来创建权重
    def build(self, input_shape):
        shape = tf.TensorShape((input_shape[1], self.output_dim))
        # 定义可训练变量
        self.weight = self.add_weight(name='weight', shape=shape, initializer='uniform', trainable=True)
        super(MyLayer, self).build(input_shape)

    def call(self, inputs):
        return tf.matmul(inputs, self.weight)

    def compute_output_shape(self, input_shape):
        shape = tf.TensorShape(input_shape).as_list()
        shape[-1] = self.output_dim
        return tf.TensorShape(shape)

    def get_config(self):
        base_config = super(MyLayer, self).get_config()
        base_config['output_dim'] = self.output_dim
        return base_config

    @classmethod
    def from_config(cls, config):
        return cls(**config)


if __name__ == '__main__':
    print()