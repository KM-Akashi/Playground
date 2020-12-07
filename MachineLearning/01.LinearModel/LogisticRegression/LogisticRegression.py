# -*- coding:UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def load_data(path="./dataset"):
    x = []
    y = []
    with open(path, 'r') as f:
        for i in f.readlines():
            line = i.replace('\n', '').split(sep=',')
            x.append(line[:-1])
            y.append([line[-1]])
    return np.array(x).astype(np.float64), np.array(y).astype(np.float64)


class RegModel(object):
    def __init__(self, data, label, learn_rate=0.1):
        self.learn_rate = learn_rate

        self.weight = np.zeros((data.shape[1]+1, 1))
        self.x = np.hstack(
            (data, np.ones((data.shape[0], 1)))
        )
        self.y = label

    def g(self, z):
        return 1/(1+np.e**(-z))

    def h(self, x):
        return self.g(np.dot(x, self.weight))

    def cost(self, y_, y):
        return - 1/(len(y)) * (y*np.log(y_) + (1-y)*np.log(1-y_))

    def dcost(self, y_, y, x):
        return - 1/(len(y)) * ((y_-y) * x)

    def train(self):
        y_ = self.h(self.x)
        self.weight -= (self.learn_rate *
                        np.sum(self.dcost(y_, self.y, self.x), axis=0)
                        ).reshape(self.weight.shape)

    def print(self):
        print('weight:\n', self.weight)


if __name__ == "__main__":
    x, y = load_data()

    model_line = RegModel(x, y)
    for _ in range(1):
        model_line.train()
    model_line.print()

    fig, ax = plt.subplots()

    pos_x = np.array([[x[i], y] for i, y in enumerate(y) if y == 1])
    neg_x = np.array([[x[i], y] for i, y in enumerate(y) if y == 0])
    ax.plot(pos_x[:, 0], pos_x[:, 1], 'b*')
    ax.plot(neg_x[:, 0], neg_x[:, 1], 'rx')

    x_ = np.arange(0, 10, step=0.1)
    # y_ = model_line.weight[0, :] * x_ + model_line.weight[1, :]
    y_ = model_line.h(
        np.hstack(
            (x_.reshape(-1,1), np.ones((x_.shape[0], 1)))
        )
    )
    ax.plot(x_, y_, 'g-')

    ax.legend()
    plt.show()
