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

    def predict(self, data):
        return self.feature[data[self.feature_name]].predict(data)

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

    def predict(self, data):
        return self.classify_name, self.classify

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


##########################################################
class RandomForest(object):
    def __init__(self, forest_size, sample_rate=0.8):
        self.forest_size = forest_size
        self.forest = list()
        self.sample_rate = sample_rate

    def fit(self, dataset):
        sample_size = int(len(dataset)*self.sample_rate)
        for _ in range(10):
            D = dataset.sample(sample_size)
            self.forest.append(C45(D, set(D.columns[:-1])))

    def predict(self, data):
        res = dict()
        for f in self.forest:
            _, classify = f.predict(data)
            if classify in res.keys():
                res[classify] += 1
            else:
                res[classify] = 1
        return res


dataset = pandas.read_csv('./dataset.csv')
rf = RandomForest(10, sample_rate=0.3)
rf.fit(dataset)

print(dataset.loc[0])
print("-----> ")
print(rf.predict(dataset.loc[0]))
