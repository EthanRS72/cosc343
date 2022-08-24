import numpy as np
import matplotlib.pyplot as plt

X = np.array([[-1, -1],
              [-1, 1],
              [1, -1],
              [1, 1]]).astype('float32')

y = np.array([0,
              0,
              0,
              1]).astype('uint8')


plt.scatter(X[:3,0], X[:3,1], c = 'red')
plt.scatter(X[3,0], X[3,1], c = 'blue')
plt.xlabel('X1')
plt.ylabel('X2')
plt.show()



#Dimensions of X
N,D = np.shape(X)
#num neurons
K = 1
#NxK matrix for Y
Y = np.expand_dims(y, axis = 1)
#epochs
max_iter = 100
#alpha
learning_rate = 0.1
#weights
W = np.random.randn(D,K)
#bias
b = np.random.randn(K)


for i in range(max_iter):
    #Step 1
    Yhat = np.dot(X, W) + b
    #step 2
    Yhat[Yhat <= 0] = 0
    Yhat[Yhat > 0] = 1
    #step 3
    E = y - Yhat
    #step 4
    tri_W = np.dot(X.T, E)
    #step 5
    tri_b = np.sum(E, axis = 0)
    #step 6
    W = W + ((learning_rate / N) * tri_W)
    b = b + ((learning_rate / N) * tri_b)
    print(np.sum(E != 0))
    if np.sum(E != 0) == 0:
        print("No Errors")
        break

