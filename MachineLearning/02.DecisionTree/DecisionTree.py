# -*- coding:UTF-8 -*-
import numpy as np
import json


def load_data(path="./dataset"):
    # 年龄、有工作、有自己房子、信贷情况、是否准贷
    data_set = []
    with open(path, 'r') as f:
        for i in f.readlines():
            line = i.replace('\n', '').split(sep=',')
            data_set.append(line[:])
    return np.array(data_set)


def H(D, A=-1):
    N = D.shape[0]
    if N == 0:
        return 0
    res = 0
    if A == -1:
        # empirical entropy
        # A = -1: H(D)
        for k in np.unique(D[:, A]):
            Ck = np.sum(D[:, A] == k)
            res -= (Ck/N)*np.log2(Ck/N)
    else:
        # empirical conditional entropy
        # A =  i: H(D|A)
        for i in np.unique(D[:, A]):
            Di_count = np.sum(D[:, A] == i)
            Di = np.vstack([vec for vec in D if vec[A] == i])
            res += (Di_count/N)*H(Di)
            # print(Di)
            # print('H(D|', i, ')=', H(Di), sep='')
    return res


def HA(D, A):
    res = 0
    for i in np.unique(D[:, A]):
        Di = [vec for vec in D if vec[A] == i]
        res -= (len(Di)/len(Di))*np.log2(len(Di)/len(Di))
    return res


def g(D, A):
    return H(D) - H(D, A)


def gR(D, A):
    return g(D, A) / H(D)


def ID3(D, A, e=0):
    if len(np.unique(D[:, -1])) == 1:
        return np.unique(D[:, -1])[0]
    if not A:
        return sorted([[k, len([vec for vec in D if vec[-1] == k])]
                       for k in np.unique(D[:, -1])],
                      key=lambda x: x[1], reverse=True)[0][0]
    G_res = sorted([[Ai, g(D, Ai)] for Ai in A],
                   key=lambda x: x[1], reverse=True)[0]
    A.remove(G_res[0])
    if G_res[1] < e:
        return sorted([[k, len([vec for vec in D if vec[-1] == k])]
                       for k in np.unique(D[:, -1])],
                      key=lambda x: x[1], reverse=True)[0][0]
    else:
        res = {}
        res[G_res[0]] = {}
        for k in np.unique(D[:, G_res[0]]):
            Di = np.vstack([vec for vec in D if vec[G_res[0]] == k])
            res[G_res[0]][k] = ID3(Di, A, e)
        return res


def C45(D, A, e=0):
    if len(np.unique(D[:, -1])) == 1:
        return np.unique(D[:, -1])[0]
    if not A:
        return sorted([[k, len([vec for vec in D if vec[-1] == k])]
                       for k in np.unique(D[:, -1])],
                      key=lambda x: x[1], reverse=True)[0][0]
    res = {}
    G_res = sorted([[Ai, gR(D, Ai)] for Ai in A],
                   key=lambda x: x[1], reverse=True)[0]
    A.remove(G_res[0])
    res[G_res[0]] = {}
    for k in np.unique(D[:, G_res[0]]):
        Di = np.vstack([vec for vec in D if vec[G_res[0]] == k])
        res[G_res[0]][k] = C45(Di, A, e)
    return res


def CART(D, A):
    res = {}
    gini_count = []
    for Ai in A:
        gini_count.extend(gini(D, Ai))
    (Ai, Ck, _) = sorted(gini_count, key=lambda x: x[2], reverse=False)[0]

    A.remove(Ai)
    res[Ai] = {}
    if A:
        other_key = ' '.join([k for k in np.unique(D[:, Ai]) if k != Ck])
        res[Ai][Ck] = CART(D, A)
        res[Ai][other_key] = sorted([[k, len([vec for vec in D if vec[-1] == k])]
                                     for k in np.unique(D[:, -1])],
                                    key=lambda x: x[1], reverse=True)[0][0]
    return res


def gini(D, A=None):
    if A is None:
        return 1 - np.sum(
            (np.asarray(
                [len([vec for vec in D if vec[-1] == k])
                 for k in np.unique(D[:, -1])]
            ) / len(D)) ** 2
        )
    else:
        res = []
        for k, Dk, Dk_ in np.asarray([
            [
                k,
                np.asarray([vec for vec in D if vec[A] == k]),
                np.asarray([vec for vec in D if vec[A] != k])
            ] for k in np.unique(D[:, A])
        ]):
            gini_Dk1 = (len(Dk)/len(D)) * gini(Dk)
            gini_Dk2 = (len(Dk_)/len(D)) * gini(Dk_)
            res.append([A, k, gini_Dk1+gini_Dk2])
        return res


if __name__ == "__main__":
    # 0年龄、1有工作、2有自己房子、3信贷情况、是否准贷
    D = load_data()
    # res = ID3(D, set(range(D.shape[1]-1)))
    # res = C45(D, set(range(D.shape[1]-1)))
    res = CART(D, set(range(D.shape[1]-1)))
    print(json.dumps(res, indent=4, ensure_ascii=False))
