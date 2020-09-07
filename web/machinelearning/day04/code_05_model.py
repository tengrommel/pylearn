import glob
import tensorflow as tf
import numpy as np
import cv2

print("TensorFlow: {}".format(tf.__version__))
classnum = {'black':0, "white": 1}
# 定义类，实现数据集的构建
class MakeTfdataset(object):

    def __init__(self):
        self.dataroot = './dataset'
        self.X_data = []
        self.Y_data = []
        self.write_data()

    def load_image(self, addr, shape=(32, 32)):
        img = cv2.imread(addr)
        img = cv2.resize(img, shape, interpolation=cv2.INTER_CUBIC)
        img = img.astype(np.float32)
        return img

    def write_data(self):
        for i in classnum.keys():
            images = glob.glob(self.dataroot + '/' + str(i) + '/*.jpg')
            labels = int(classnum)
            print(labels, '\t\t', i)
            for img in images:
                img = self.load_image(img)
                self.X_data.append(img)
                self.Y_data.append(labels)

    def read_data(self):
        self.X_data = np.array(self.X_data)
        self.Y_data = np.array(self.Y_data)
        dx_train = tf.data.Dataset.from_tensor_slices(self.X_data)
        dy_train = tf.data.Dataset.from_tensor_slices(self.Y_data).map(lambda z: tf.one_hot(z, len(classnum)))
        train_dataset = tf.data.Dataset.zip((dx_train, dy_train)).shuffle(50000).repeat().batch(256).prefetch(tf.data.experimental.AUTOTUNE)
        return train_dataset

