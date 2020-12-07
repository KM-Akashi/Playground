# -*- coding:UTF-8 -*-
import numpy as np
import random
import cvxopt

import matplotlib.pyplot as plt
import matplotlib.colors


def load_data(path="./dataset"):
    point = []
    label = []
    with open(path, 'r') as f:
        for i in f.readlines():
            line = i.replace('\n', '').split(sep=',')
            point.append(line[0:-1])
            label.append([line[-1]])
    return np.matrix(point).astype(np.float64), np.matrix(label).astype(np.float64)


class SupportVectorMachines(object):
    def __init__(self, point, label, C=1, kernel=None):
        self.point = point
        self.label = label
        self.C = C
        if kernel is None:
            self.kernel = self.linear_kernel
        else:
            self.kernel = kernel
        cvxopt.solvers.options['show_progress'] = False

        self.alpha = None

    @staticmethod
    def linear_kernel(xi, xj):
        return xi * xj.T

    @staticmethod
    def sign_func(x):
        if x < 0:
            return -1
        elif x > 0:
            return 1
        else:
            return 1

    def decision(self, x, sign=True):
        if sign:
            return self.sign_func(
                np.sum(np.multiply(
                    self.alpha,
                    np.multiply(
                        self.label,
                        self.kernel(self.point, x)
                    )
                )) + self.bias()
            )
        else:
            return np.sum(np.multiply(
                self.alpha,
                np.multiply(
                    self.label,
                    self.kernel(self.point, x)
                )
            )) + self.bias()

    def weight(self):
        return np.sum(
            np.multiply(
                np.multiply(self.alpha, self.label),
                self.point),
            axis=0
        )

    def bias(self):
        bias_count = len([self.alpha for a in self.alpha if a != 0])
        bias = 0
        if bias_count == 0:
            return bias
        else:
            for i, ai in enumerate(self.alpha):
                if ai[0] > 0 and ai[0] < self.C:
                    bias += self.label[i, 0] - \
                        np.sum(
                            np.multiply(
                                np.multiply(self.alpha, self.label),
                                self.point *
                                self.point[i, :].reshape(-1, 1)
                            ))
            return bias/bias_count

    def minimize_HM(self):
        # Hard Margin
        extend_point = np.column_stack(
            (self.point, np.ones((self.point.shape[0], 1))))
        P = cvxopt.matrix([[1.0, 0.0, 0.0],
                           [0.0, 1.0, 0.0],
                           [0.0, 0.0, 0.0]])
        q = cvxopt.matrix([0.0, 0.0, 0.0])

        G = cvxopt.matrix(-np.multiply(self.label, extend_point))
        h = cvxopt.matrix(-np.ones((extend_point.shape[0], 1)))

        sol = cvxopt.solvers.qp(P, q, G, h)

        return np.array(
            list(map(lambda x: round(x, 2), sol['x']))
        ).reshape(-1)

    def minimize_HM_dual(self):
        # dual Hard Margin
        P = cvxopt.matrix(
            np.multiply(
                self.label * self.label.T,
                self.kernel(self.point, self.point)
            ))
        q = cvxopt.matrix(-np.ones(self.label.shape))

        G = cvxopt.matrix(-np.eye(self.label.shape[0]))
        h = cvxopt.matrix(np.zeros(self.label.shape))

        A = cvxopt.matrix(self.label.T)
        b = cvxopt.matrix([0.0])

        sol = cvxopt.solvers.qp(P, q, G, h, A, b)

        self.alpha = np.matrix(
            list(map(lambda x: round(x, 2), sol['x']))
        ).reshape(-1, 1)
        return self.alpha

    def minimize_SM_dual(self):
        # dual Soft Margin
        P = cvxopt.matrix(
            np.multiply(
                self.label * self.label.T,
                self.kernel(self.point, self.point)
            ))
        q = cvxopt.matrix(-np.ones(self.label.shape))

        G = cvxopt.matrix(
            np.vstack((
                -np.eye(self.label.shape[0]),
                np.eye(self.label.shape[0])))
        )
        h = cvxopt.matrix(
            np.vstack((
                np.zeros(self.label.shape),
                self.C * np.ones(self.label.shape)
            ))
        )

        A = cvxopt.matrix(self.label.T)
        b = cvxopt.matrix([0.0])

        sol = cvxopt.solvers.qp(P, q, G, h, A, b)

        self.alpha = np.matrix(
            list(map(lambda x: round(x, 2), sol['x']))
        ).reshape(-1, 1)
        return self.alpha

    def SMO(self, max_epoch=100):
        self.alpha = np.ones(
            self.point.shape[0]
        ).reshape(-1, 1) * random.random() * self.C
        # 根据KKT条件选取第一个，根据E选取第二个
        for _ in range(max_epoch):
            E_list = np.array([
                self.decision(x, sign=False)
                for x in self.point
            ])
            for i, x in enumerate(self.label * self.decision(self.point, sign=False)):
                if not self.KKY_test(self.alpha[i], x):
                    j = -1
                    if E_list[i] >= 0:
                        j = sorted(enumerate(E_list),
                                   key=lambda x: x[1])[0][0]
                    print(i, j)
            break

    def KKY_test(self, a, d):
        if (a == 0 and d >= 1) or (a > 0 and a < self.C and d == 1) or (a == self.C and d <= 1):
            return True
        else:
            return False


def printPlot(svm):
    alpha = svm.alpha
    point, label = svm.point, svm.label
    x_ = np.linspace(0, 5, num=50)
    X1_, X2_ = np.meshgrid(x_, x_)
    res = []
    for i in range(len(x_)):
        for j in range(len(x_)):
            res.append(
                svm.decision(
                    np.matrix([[x_[i], x_[j]]])
                )
            )
    res = np.array(res).reshape(-1, len(x_))
    plt.contourf(X1_, X2_, res,
                 cmap=matplotlib.colors.ListedColormap(('lightblue', 'lightyellow')))

    if alpha is not None:
        sv_x1 = [point[i, 0] for i, ai in enumerate(alpha) if ai[0] != 0]
        sv_x2 = [point[i, 1] for i, ai in enumerate(alpha) if ai[0] != 0]
        plt.scatter(sv_x1, sv_x2, c='w', marker='o', edgecolors='g', s=100)

    pos_x1 = [point[i, 0] for i, l in enumerate(label) if l[0] == 1]
    pos_x2 = [point[i, 1] for i, l in enumerate(label) if l[0] == 1]
    plt.scatter(pos_x1, pos_x2, c='r', marker='+')
    neg_x1 = [point[i, 0] for i, l in enumerate(label) if l[0] == -1]
    neg_x2 = [point[i, 1] for i, l in enumerate(label) if l[0] == -1]
    plt.scatter(neg_x1, neg_x2, c='b', marker='x')

    plt.show()


if __name__ == "__main__":
    data_point, data_label = load_data()

    def polynomial_kernel(xi, xj, delte=1):
        if delte < 1:
            delte = 1
        return np.asarray(np.dot(xi, xj.T))**delte

    def gauss_kernel(xi, xj, delte=1):
        if delte <= 0:
            delte = 1
        return np.exp(- (np.linalg.norm(xi-xj, ord=2, axis=1)**2) / (2 * delte**2)).reshape(-1, 1)

    def laplace_kernel(xi, xj, delte=1):
        if delte <= 0:
            delte = 1
        return np.exp(- (np.linalg.norm(xi-xj, ord=2, axis=1)) / delte).reshape(-1, 1)

    svm = SupportVectorMachines(data_point, data_label,
                                kernel=None)
    # svm.minimize_SM_dual()
    svm.SMO()

    print(svm.alpha)
    printPlot(svm)
