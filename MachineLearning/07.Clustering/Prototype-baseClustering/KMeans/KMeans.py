import numpy as np

import matplotlib.pyplot as plt


def load_data(path="./dataset"):
    point = []
    with open(path, 'r') as f:
        for i in f.readlines():
            line = i.replace('\n', '').split(sep=',')
            point.append(line[:])
    return np.array(point).astype(np.float64)


def kMeans(data, k):
    mean_vecs = np.array(
        [data[i] for i in np.random.randint(data.shape[0], size=K)]
    )
    C = {i: list() for i in range(mean_vecs.shape[0])}

    CHANGED = True
    while CHANGED:
        for xi in data:
            C[
                sorted(
                    [[mi, np.linalg.norm(xi-mv, ord=2)]
                     for mi, mv in enumerate(mean_vecs)],
                    key=lambda x: x[1]
                )[0][0]
            ].append(xi)

        CHANGED_COUNT = 0
        for k in C.keys():
            mv = np.sum(C[k], axis=0) / len(C[k])
            if (mv != mean_vecs[k]).all():
                mean_vecs[k] = mv
                CHANGED_COUNT += 1
        if CHANGED_COUNT == 0:
            CHANGED = False

    return mean_vecs


if __name__ == "__main__":
    data = load_data()
    K = 2

    plt.scatter(data[:, 0], data[:, 1], c='k', marker='o')

    mean_vecs = kMeans(data, K)

    plt.scatter(mean_vecs[:, 0], mean_vecs[:, 1], c='r', marker='x', s=100)
    plt.show()
