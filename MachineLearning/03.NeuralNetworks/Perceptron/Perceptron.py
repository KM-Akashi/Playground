# -*- coding:UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def load_data(path="./dataset"):
    train_x = []
    train_y = []
    with open(path, 'r') as f:
        for i in f.readlines():
            line = i.replace('\n', '').split(sep=',')
            train_x.append(line[0:-1])
            train_y.append([line[-1]])
    return np.array(train_x).astype(np.float64), np.array(train_y).astype(np.float64)


class Node(object):
    def __init__(self, data_x, data_y, rate=0.01):
        self.data_x = data_x
        self.data_y = data_y
        self.rate = rate

        self.data_shape = data_x.shape

        self.weight = np.zeros((self.data_shape[1], 1))
        self.bias = np.zeros(1)

    def sign(self, x):
        f = np.dot(x, self.weight) + self.bias
        if f >= 0:
            return 1
        else:
            return -1

    def check(self):
        flag = True
        for index in range(self.data_shape[0]):
            if self.sign(self.data_x[index, :]) * self.data_y[index] < 0:
                flag = False
                break
        return flag

    def fit(self):
        while True:
            for index in range(self.data_shape[0]):
                if self.sign(self.data_x[index, :]) * self.data_y[index] <= 0:
                    self.weight += self.rate * self.data_y[index] * \
                        self.data_x[index, :].reshape(self.data_shape[1], -1)
                    self.bias += self.rate * self.data_y[index]
            if self.check():
                break


if __name__ == "__main__":
    x, y = load_data()
    node = Node(x, y)
    node.fit()
    print("w:\n", node.weight)
    print("b:\n", node.bias)
