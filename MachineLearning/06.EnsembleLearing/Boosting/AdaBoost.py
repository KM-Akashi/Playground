import numpy as np


class AdaBoostNode(object):
    # x = np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    # y = np.asarray([1, 1, 1, -1, -1, -1, 1, 1, 1, -1])
    def __init__(self):
        self.found = False
        self.flag = 1
        self.bias = 0
        self.right_rate = 0

    def fit(self, x, y):
        right_sort = list()
        for x_ in np.unique(x):
            result = [
                1 if self.predict(xi, x_, 1) == y[i] else 0
                for i, xi in enumerate(x)
            ]
            right_rate = sum(result) / len(result)
            if right_rate >= 0.5:
                right_sort.append((x_, 1, right_rate))
            else:
                right_sort.append((x_, -1, 1-right_rate))
        right_sort.sort(key=lambda x: x[2], reverse=True)
        self.bias = right_sort[0][0]
        self.flag = right_sort[0][1]
        self.right_rate = right_sort[0][2]

    def predict(self, xi, bias=None, flag=None):
        if bias is None:
            bias = self.bias
        if flag is None:
            flag = self.flag
        return flag if xi < bias else -1*flag


class AdaBoost(object):
    def __init__(self, nodes, raw_data, sample_size=1000):
        self.nodes = nodes
        self.raw_data = raw_data
        self.sample_weight = np.ones(len(raw_data)) / len(raw_data)
        self.sample_size = sample_size
        self.node_weight = list()

    def fit(self):
        for node in self.nodes:
            sample = np.asarray([
                raw_data[i]
                for i in np.random.choice(
                    range(self.raw_data.shape[0]),
                    p=self.sample_weight,
                    size=self.sample_size)
            ])
            x = sample[:, :-1].reshape(-1)
            y = sample[:, -1].reshape(-1)
            node.fit(x, y)

            y_ = [node.predict(xi) for xi in self.raw_data[:, :-1].reshape(-1)]
            result = [
                1 if yi == y_[i] else -1
                for i, yi in enumerate(self.raw_data[:, -1].reshape(-1))
            ]
            error_rate = sum([1 for i in result if i != 1]) / len(y_)
            alpha = np.log((1-error_rate) / error_rate) / 2
            self.node_weight.append(alpha)
            self.sample_weight = [
                wi * np.exp(-alpha*result[i])
                for i, wi in enumerate(self.sample_weight)
            ]
            self.sample_weight = self.sample_weight / sum(self.sample_weight)

    def predict(self, x):
        result = [node.predict(x) * self.node_weight[i]
                  for i, node in enumerate(self.nodes)]
        return 1 if sum(result) >= 0 else -1


raw_data = np.asarray([
    [0, 1],
    [1, 1],
    [2, 1],
    [3, -1],
    [4, -1],
    [5, -1],
    [6, 1],
    [7, 1],
    [8, 1],
    [9, -1]
])

nodes = [AdaBoostNode() for i in range(10)]
boosting = AdaBoost(nodes, raw_data)
boosting.fit()

for i in range(10):
    print(raw_data[i][0], "<->", boosting.predict(i), raw_data[i][1])
