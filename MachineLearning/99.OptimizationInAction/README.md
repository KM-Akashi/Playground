# Optimization In Action


## Question
min f(x) = (x+1)^2 + y^2

## Usage

f(x) = (x+1)^2 + y^2
g(x) = 2(x+1)i + 2yj

> Note:
> g(x) is gradient of f(x).
> x0 is initialization parameter.

```python 
    def f(x): return (x[0] + 1)**2 + x[1]**2

    def g(x): return np.array([
        2*(x[0] + 1),
        2*x[1]
    ])
    x0 = np.array([10, -10])

    DFP(f, g, x0)
    BFGS(f, g, x0)
```

Then x0 will be converged to the nearest minimum value point of f(x) by Quasi-Newton methods.

## Output

Minimum value point of f(x, y) = (x+1)^2 + y^2  is ```[-1.  0.]```

```bash
DFP[26]: [-9.99996247e-01 -3.41163456e-06]
DFP:  [-9.99997748e-01 -2.04698074e-06]
BFGS[8]: [-9.99994368e-01 -5.12000000e-06]
BFGS: [-9.99998874e-01 -1.02400000e-06]
```

While line search step is 5 (50% gradient), DFP returns result in 26 iterations, BFHS returns result in 8 iterations.
