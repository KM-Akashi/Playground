# SupportVectorMachines
> 支持向量机

## Catalogs
- 线性可分支持向量机学习算法 最大间隔法

- 线性支持向量机学习算法

- 非线性支持向量机算法

- SMO算法

---

## 最优化问题
1. 最优化问题的一般形式：
$ minimize\ f_{0}(x) $
$ s.t. $
$ \qquad f_{i}(x) \leq 0 \qquad i=1,…,m $
$ \qquad h_{i}(x) = 0 \qquad i=1,…,p $

2. 定义Lagrangian函数：
$ L(x,\lambda,\nu) = f_{0}(x) + \sum_{i=1}^{m}\lambda_{i}f_{i}(x) + \sum_{i=1}^{p}\nu_{i}h_{i}(x) $

3. KKT条件：
$ \bigtriangledown f_{0}(x^*) + \sum_{i=1}^{m}\lambda_{i}^*\bigtriangledown f_{i}(x^*) + \sum_{i=1}^{p}\nu_{i}^*\bigtriangledown h_{i}(x^*) = 0 $
$ h_{i}(x^*) = 0  ,\ i=1,…,p $
$ \lambda_{i}^*f_{i}(x^*) = 0,\ i=1,…,m $
$ f_{i}(x^*) \leq 0 ,\ i=1,…,m $
$ \lambda_{i}^* \geq 0  ,\ i=1,…,m $

## 最优化问题 例子
$ minimize\ 10-x_{1}^{2}-x_{2}^{2} $
$ s.t. \qquad x_2 \geq x_1^2,x_1+x_2=0 $

构造Lagrangigan乘子式
$ L = (10 - x_1^2 - x_2^2) + \lambda (x_1^2 - x_2) + \nu (x_1 + x_2) $

代码
```python
from sympy import *

x1 = Symbol("x1")
x2 = Symbol("x2")
a = Symbol("a")
b = Symbol("b")
f = 10 - x1**2 - x2**2 + a*(x1 + x2) + b*(x1**2 - x2)
fx1 = diff(f, x1)
fx2 = diff(f, x2)
result = solve([fx1, fx2, (x1**2-x2)*b, x1+x2], [x1, x2, a, b])

for r in result:
    if r[3] >= 0 and \
        r[0]**2-r[1] <= 0 and \
            r[2] != 0:
        print(r)
        print("loss:", 10 - r[0]**2 - r[1]**2 + r[2]
              * (r[1] + r[0]) + r[3]*(r[0]**2 - r[1]))
```