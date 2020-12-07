import numpy as np

DATA_SET = np.array([
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
])


def nonlin(x, deriv=False):
    # sigmoid function
    if deriv:
        return x*(1-x)
    else:
        return 1/(1+np.exp(-x))


class Layer(object):
    def __init__(self, in_feature, out_feature, activation_function):
        # x ∈ [-1, 1]
        self.shape = (in_feature, out_feature)
        self.weight = 2*np.random.random((in_feature, out_feature)) - 1
        # TODO:
        # self.bias = 2*np.random.random((out_feature, 1)) - 1
        self.bias = 0
        self.func = activation_function

    def forward(self, x):
        return self.func(np.dot(x, self.weight) + self.bias).reshape(-1, self.shape[1])

    def backward(self, error, y_):
        delta = error * self.func(y_, deriv=True)
        return delta


l1 = Layer(3, 4, nonlin)
l2 = Layer(4, 1, nonlin)

MAX_EPOCHS = 10000
for epoch in range(MAX_EPOCHS):
    x = DATA_SET[:, :3]
    y = DATA_SET[:, 3:]

    y_1 = l1.forward(x)
    y_2 = l2.forward(y_1)

    d_2 = l2.backward(y - y_2, y_2)
    d_1 = l1.backward(d_2.dot(l2.weight.T), y_1)

    l2.weight += y_1.T.dot(d_2)
    l1.weight += x.T.dot(d_1)


print('HERE')
x = DATA_SET[:, :3]
y_1 = l1.forward(x)
y_2 = l2.forward(y_1)
print(y_2)
