import numpy as np


def F(N):
    return 1 if N <= 1 else N * F(N-1)


def A(N, M):
    assert(N >= M)
    return int(F(N) / F(N-M))


def C(N, M):
    assert(N >= M)
    return int(A(N, M) / F(M))


def P(p, m, n):
    # 发生概率为p的事件在总事件数为N次的实验中发生了M次
    return C(n, m) * p**m * (1-p)**(n-m)


def sample_prob(sample, prob):
    # sample 在 prob 下的概率
    n = sum(sample)
    return sum([P(prob[i], s, n) for i, s in enumerate(sample)])


class ExpectationMaximum(object):
    def __init__(self, SAMPLE_DATA, classes_size):
        self.SAMPLE_DATA = np.asarray(SAMPLE_DATA)
        self.classes_size = classes_size
        self.feature_size = SAMPLE_DATA.shape[1]
        self.prob = np.random.random((self.classes_size, self.feature_size))
        for i, p in enumerate(self.prob):
            self.prob[i] = self.prob[i] / sum(self.prob[i])

    def E(self):
        result = list()
        for s_i, sample in enumerate(self.SAMPLE_DATA):
            result.append(
                (
                    s_i,
                    sorted(
                        [
                            (p_i, sample_prob(sample, p))
                            for p_i, p in enumerate(self.prob)
                        ],
                        key=lambda x: x[1],
                        reverse=True
                    )[0][0]
                )  # （样本Index，类别Index）
            )
        return result

    def M(self, result):
        for i in range(self.classes_size):
            new_sample = np.asarray([
                self.SAMPLE_DATA[s_i]
                for s_i, p_i in result if p_i == i
            ])
            new_sample_size = sum([sum(s) for s in new_sample])
            if new_sample_size == 0:
                pass
            else:
                for j in range(self.feature_size):
                    self.prob[i, j] = sum(new_sample[:, j]) / new_sample_size


SAMPLE_DATA = [
    # H T
    [5, 5],
    [9, 1],
    [8, 2],
    [4, 6],
    [7, 3]
]
SAMPLE_DATA = np.asarray(SAMPLE_DATA)
e = ExpectationMaximum(SAMPLE_DATA, 2)
print('=>\n', e.prob)
e.M(e.E())
print('=>\n', e.prob)
e.M(e.E())
print('=>\n', e.prob)
e.M(e.E())
print('=>\n', e.prob)
e.M(e.E())
print('=>\n', e.prob)
