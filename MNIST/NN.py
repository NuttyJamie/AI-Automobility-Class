import numpy as np

def sigmoid(x):
	return 1/(1+np.exp(-x))

X=np.array([0, 1])
W1=np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1=np.array([0.1, 0.2, 0.3])
W2=np.array([[0.2, 0.4], [0.6, 0.1], [0.1, 0.2]])
B2=np.array([0.3, 0.3])
W3=np.array([[0.2, 0.5, 0.2], [0.1, 0.1, 0.2]])
B3=np.array([0.1, 0.2, 0.1])

A1=np.dot(X, W1)+B1
Z1=sigmoid(A1)
A2=np.dot(Z1,W2)+B2
Z2=sigmoid(A2)
A3=np.dot(Z2,W3)+B3

print(A3)
