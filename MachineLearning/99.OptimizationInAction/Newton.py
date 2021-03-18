import numpy as np


def line_search(f, x0, p, step=1e-1, k=5):
    min_x = x0
    min_f = f(x0)
    for i in range(k):
        xk = x0 + p * (i*step)
        if f(xk) < min_f:
            min_f = f(xk)
            min_x = xk
    return min_x


def DFP(f, g, x0, k_max=800, e=1e-5):
    if np.linalg.norm(g(x0), ord=2) < e:
        return x0

    x = x0
    G = np.eye(x0.shape[0])
    for k in range(k_max):
        gx = g(x)
        p = - np.dot(G, gx.reshape(gx.shape[0], 1)).reshape(-1)
        x_ = line_search(f, x, p)
        gx_ = g(x_)
        if np.linalg.norm(gx_, ord=2) < e:
            print('\nDFP: ', x_)
            return x_
        else:
            dgT = (gx - gx_).reshape((1, G.shape[0]))
            dg = dgT.reshape((dgT.shape[1], 1))
            dxT = (x - x_).reshape((1, G.shape[0]))
            dx = dxT.reshape((dxT.shape[1], 1))

            G += np.dot(dx, dxT) / \
                np.dot(dxT, dg) - \
                np.dot(np.dot(np.dot(G, dg), dgT), G) / \
                np.dot(np.dot(dgT, G), dg)
            x = x_
            print('\rDFP[', k, ']: ', x, sep='', end='')
    print('\nDFP: ', None)
    return None


def BFGS(f, g, x0, k_max=800, e=1e-5):
    if np.linalg.norm(g(x0), ord=2) < e:
        return x0

    x = x0
    B = np.eye(x0.shape[0])
    for k in range(k_max):
        gx = g(x)
        p = - np.dot(np.linalg.inv(B), gx.reshape(gx.shape[0], 1)).reshape(-1)
        x_ = line_search(f, x, p)
        gx_ = g(x_)
        if np.linalg.norm(gx_, ord=2) < e:
            print('\nBFGS:', x_)
            return x_
        else:
            dgT = (gx - gx_).reshape((1, B.shape[0]))
            dg = dgT.reshape((dgT.shape[1], 1))
            dxT = (x - x_).reshape((1, B.shape[0]))
            dx = dxT.reshape((dxT.shape[1], 1))

            B += np.dot(dg, dxT) / \
                np.dot(dgT, dx) - \
                np.dot(np.dot(np.dot(B, dx), dxT), B) / \
                np.dot(np.dot(dxT, B), dx)
            x = x_
            print('\rBFGS[', k, ']: ', x, sep='', end='')
    print('\nBFGS:', None)
    return None


if __name__ == "__main__":
    def f(x): return (x[0] + 1)**2 + x[1]**2

    def g(x): return np.array([
        2*(x[0] + 1),
        2*x[1]
    ])
    x0 = np.array([10, -10])

    #########################
    # def f(x): return x[0]**2 + 1
    #
    # def g(x): return np.array([
    #     2*x[0]
    # ])
    # x0 = np.array([10])
    #########################

    DFP(f, g, x0)
    BFGS(f, g, x0)
    pass
