# -*- coding:UTF-8 -*-
import numpy as np
import collections


def load_data(path="./dataset"):
    train_x = []
    train_y = []
    with open(path, 'r') as f:
        for i in f.readlines():
            line = i.replace('\n', '').split(sep=',')
            train_x.append(line[0:-1])
            train_y.append([line[-1]])
    return np.array(train_x).astype(np.float64), np.array(train_y).astype(np.float64)


def distanc(x, y, p=2):
    if x.shape != y.shape:
        return -1
    else:
        return np.linalg.norm(np.fabs(x-y), ord=p)


def k_NN(x, data_x, data_y, k=3, p=2):
    dis_list = np.array(
        sorted([[data_y[i, 0], distanc(x, xi)]
                for i, xi in zip(range(len(data_x)), data_x)],
               key=lambda x: x[1])
    )
    return sorted(collections.Counter(dis_list[0:k, 0]).items(),
                  key=lambda i: i[1])[0][0]


class kd_tree_node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def display(self):
        return (self.value,
                [self.left.display() if self.left is not None else None,
                 self.right.display() if self.right is not None else None])

    def DLR(self):
        print(self.value)
        if self.left is not None:
            self.left.LDR()
        if self.right is not None:
            self.right.LDR()

    def LDR(self):
        if self.left is not None:
            self.left.LDR()
        print(self.value)
        if self.right is not None:
            self.right.LDR()


def kd_tree(data_set, k, i=0):
    data_set = sorted(data_set, key=lambda x: x[i])
    l = len(data_set)
    if l == 0:
        return None
    elif l == 1:
        return kd_tree_node(data_set[0])
    else:
        m = int(l/2)
        return kd_tree_node(data_set[m],
                            left=kd_tree(data_set[:m], k, (i+1) % k),
                            right=kd_tree(data_set[m + 1:], k, (i+1) % k)
                            )


def nearest_neighbor_search(root, point):
    next = root
    i = 0
    k = root.value.shape[0]
    path = []
    while True:
        path.append(next)
        if next.right is None and next.left is None:
            break
        if next.right is None and next.left is not None:
            next = next.left
        elif next.right is not None and next.left is None:
            next = next.right
        elif point[i] < next.value[i]:
            next = next.left
        else:
            next = next.right
        i = (i+1) % k

    nearest = path[-1]
    for p in path[::-1]:
        if distanc(point, nearest.value) > distanc(point, p.value):
            nearest = p
    return nearest


if __name__ == "__main__":
    data_x, data_y = load_data()
    x = np.array([1.5, 1.5])
    print('k_NN: k=3', x, 'is', k_NN(x, data_x, data_y, k=3))

    print('-'*10)

    data_set = np.array([[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]])
    root = kd_tree(data_set, data_set.shape[1])
    print('kd tree:', root.display())
    print('-'*10)
    point = np.array([4, 4])
    print(point, 'nearest neighbor:', nearest_neighbor_search(root, point).value)
