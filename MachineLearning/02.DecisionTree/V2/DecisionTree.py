import numpy
import pandas
from pandas.core.frame import DataFrame


class TreeNode(object):
    def __init__(self, feature_name):
        self.single_node = False
        self.feature_name = feature_name
        self.feature = dict()

    def setFeature(self, feature, node):
        self.feature[feature] = node

    def isSingle(self):
        return self.single_node

    def print(self, dep=0):
        for feature in self.feature.keys():
            print("    "*dep, "-{}, {}".format(self.feature_name, feature), sep='')
            self.feature[feature].print(dep+1)


class SingleTreeNode(object):
    def __init__(self, classify_name, classify):
        self.single_node = True
        self.classify_name = classify_name
        self.classify = classify

    def isSingle(self):
        return self.single_node

    def print(self, dep=0):
        print("    "*dep, "-{}-> {}".format(self.classify_name, self.classify), sep='')


##########################################################
def H(D, A=None):
    res = 0
    if len(D) == 0:
        return 0
    if A is None:
        classify_name = D.columns[-1]
        for k in D[classify_name].unique():
            Ck = D.loc[D[classify_name] == k]
            res -= (len(Ck)/len(D)) * numpy.log2((len(Ck)/len(D)))
    else:
        feature_name = A
        for Ai in D[feature_name].unique():
            Di = D.loc[D[feature_name] == Ai]
            res += (len(Di)/len(D)) * H(Di)
    return res


def HA(D, A):
    res = 0
    for Ai in D[A].unique():
        Di = D.loc[D[A] == Ai]
        res -= (len(Di)/len(D)) * numpy.log2(len(Di)/len(D))
    return res


def g(D, A):
    return H(D) - H(D, A)


def gR(D, A):
    return g(D, A) / H(D)


def ID3(D: DataFrame, A: set, e=0):
    classify_name = D.columns[-1]
    if len(D[classify_name].unique()) == 1:
        return SingleTreeNode(classify_name, D[classify_name].unique()[0])
    if not A:
        return SingleTreeNode(classify_name, D[classify_name].value_counts().index[0])

    G_res = sorted(
        [
            [Ai, g(D, Ai)]
            for Ai in A
        ],
        key=lambda x: x[1],
        reverse=True
    )
    Ag = G_res[0][0]
    error = G_res[0][1]
    A.remove(Ag)

    if error < e:
        return SingleTreeNode(classify_name, D[classify_name].value_counts().index[0])
    else:
        tree = TreeNode(Ag)
        for feature in D[Ag].unique():
            Di = D.loc[D[Ag] == feature]
            tree.setFeature(feature, ID3(Di, A, e))
        return tree


def C45(D: DataFrame, A: set, e=0):
    classify_name = D.columns[-1]
    if len(D[classify_name].unique()) == 1:
        return SingleTreeNode(classify_name, D[classify_name].unique()[0])
    if not A:
        return SingleTreeNode(classify_name, D[classify_name].value_counts().index[0])

    G_res = sorted(
        [
            [Ai, gR(D, Ai)]
            for Ai in A
        ],
        key=lambda x: x[1],
        reverse=True
    )
    Ag = G_res[0][0]
    error = G_res[0][1]
    A.remove(Ag)

    if error < e:
        return SingleTreeNode(classify_name, D[classify_name].value_counts().index[0])
    else:
        tree = TreeNode(Ag)
        for feature in D[Ag].unique():
            Di = D.loc[D[Ag] == feature]
            tree.setFeature(feature, C45(Di, A, e))
        return tree


def gini(D, A=None):
    if A is None:
        gini_sum = 0
        classify_name = D.columns[-1]
        for k in D[classify_name].unique():
            Ck = D.loc[D[classify_name] == k]
            gini_sum += (len(Ck)/len(D))**2
        gini_sum = 1 - gini_sum
        return gini_sum
    else:
        feature_name = A
        gini_sort = list()
        for Ai in D[feature_name].unique():
            D1 = D.loc[D[feature_name] == Ai]
            D2 = D.loc[D[feature_name] != Ai]
            gini_1 = (len(D1)/len(D))*gini(D1)
            gini_2 = (len(D2)/len(D))*gini(D2)
            gini_sort.append(
                [A, Ai, gini_1+gini_2]
            )
        return gini_sort


def CART(D: DataFrame, A: set, e=0, gini_e=0):
    classify_name = D.columns[-1]
    if not A or len(D) < e:
        return SingleTreeNode(classify_name, D[classify_name].unique()[0])

    gini_sort = list()
    for a in A:
        gini_sort.extend(gini(D, a))
    (Ai, ai, gi) = sorted(gini_sort, key=lambda x: x[2], reverse=False)[0]

    if gi < gini_e:
        return SingleTreeNode(classify_name, D[classify_name].unique()[0])

    tree = TreeNode(Ai)
    D1 = D.loc[D[Ai] == ai]
    D2 = D.loc[D[Ai] != ai]
    A.remove(Ai)
    tree.setFeature(ai, CART(D1, A, e, gini_e))
    tree.setFeature("otherwise", CART(D2, A, e, gini_e))
    return tree


##########################################################
# TODO 剪枝
dataset = pandas.read_csv('./dataset.csv')
print("*"*10, "ID3", "*"*10)
ID3(dataset, set(dataset.columns[:-1])).print()
print("*"*10, "C45", "*"*10)
C45(dataset, set(dataset.columns[:-1])).print()
print("*"*10, "CART", "*"*10)
CART(dataset, set(dataset.columns[:-1])).print()
