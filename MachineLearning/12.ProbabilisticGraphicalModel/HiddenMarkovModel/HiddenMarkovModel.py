import numpy as np
from pandas import DataFrame

Q = ["盒子1", "盒子2", "盒子3"]
V = ["红", "白"]

pi = np.asarray([0.2, 0.4, 0.4])

pro_a = np.asarray([[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.3, 0.5]])
A = DataFrame(pro_a, columns=Q, index=Q)

pro_b = np.asarray([[0.5, 0.5], [0.4, 0.6], [0.7, 0.3]])
B = DataFrame(pro_b, columns=V, index=Q)

# T = 3
O = ["红", "白", "红"]

lam = (A, B, pi)


def forward(O, lam):
    (A, B, pi) = lam
    alpha = list()
    for i, oi in enumerate(O):
        if i == 0:
            alpha.append(pi * np.asarray(B[O[0]]))
        else:
            alpha.append(
                np.asarray([sum(alpha[-1] * np.asarray(A[ai]))
                            for ai in A]) * np.asarray(B[oi]))
    return sum(alpha[-1]), np.asarray(alpha)


def backward(O, lam):
    (A, B, pi) = lam
    beta = list()
    beta.append(np.ones_like(A.columns))
    for i, oi in enumerate(O[::-1]):
        if i == len(O) - 1:
            beta.append(pi * np.asarray(B[oi]) * beta[-1])
        else:
            beta.append(
                np.asarray([
                    sum(np.asarray(A.loc[ai]) * np.asarray(B[oi]) * beta[-1])
                    for ai in A.columns
                ]))
    beta = beta[-1:0:-1]
    return sum(beta[0]), np.asarray(beta)


class BaumWelch(object):
    # TODO
    def __init__(self, Q, V):
        pro_a = np.ones((len(Q), len(Q)))
        pro_a /= np.sum(pro_a)
        pro_b = np.ones((len(Q), len(V)))
        pro_b /= np.sum(pro_b)
        pi = np.ones((1, len(Q)))
        pi /= np.sum(pi)
        self.A = DataFrame(pro_a, columns=Q, index=Q)
        self.B = DataFrame(pro_b, columns=V, index=Q)
        self.pi = pi

    def fit(self, O):
        _, alpha = forward(O, lam)
        _, beta = backward(O, lam)
        gramma = alpha * beta
        gramma = np.asarray([t / np.sum(t) for t in gramma])


class Viterbi(object):
    # TODO
    def __init__(self, Q, V):
        pass


# pro, alpha = forward(O, lam)
# pro, beta = backward(O, lam)

b = BaumWelch(Q, V)
b.fit(O)
