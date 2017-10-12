import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def draw_3D(Z,X_SIZE,Y_SIZE):
    '''
    fig = plt.figure()
    #ax = fig.add_subplot(111, projection = '3d')
    X = [0 for i in range(X_SIZE * Y_SIZE)]
    Y = [0 for i in range(X_SIZE * Y_SIZE)]
    R = [0 for i in range(X_SIZE * Y_SIZE)]

    for i in range(X_SIZE):
        for j in range(Y_SIZE):
            X[i * X_SIZE + j] = i
            Y[i * X_SIZE + j] = j
            R[i * X_SIZE + j] = Z[i][j][1]
    f = plt.plot_trisurf(X,Y,R)
    plt.show()
    '''

    X = [0 for i in range(X_SIZE * Y_SIZE)]
    Y = [0 for i in range(X_SIZE * Y_SIZE)]
    R = [0 for i in range(X_SIZE * Y_SIZE)]
    for i in range(X_SIZE):
        for j in range(Y_SIZE):
            X[i * X_SIZE + j] = i
            Y[i * X_SIZE + j] = j
            R[i * X_SIZE + j] = Z[i][j][1]
    cm=plt.cm.get_cmap('RdYlBu')
    sc=plt.scatter(X,Y,c=R,vmin=-90,vmax=-65,s=35,cmap=cm)
    plt.colorbar(sc)
    plt.show()

    return