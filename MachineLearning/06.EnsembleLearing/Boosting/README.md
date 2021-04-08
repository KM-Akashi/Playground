# AdaBoost
Ada提升方法

Gm(x)系数：
error_rate 错误率
alpha_m = np.log((1-error_rate) / error_rate) / 2

更新样本采样权值：
wi = wi * np.exp(-alpha * error?)

最终分类器：
node.predict(x) * self.node_weight[i]