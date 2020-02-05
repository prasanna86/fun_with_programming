'''
Y = a + b1.f1 + b2.f2 + ... + bm.fm = g(f1, f2, ..., fm; beta) 
where beta = (a, b1, b2, bm) are model params and Features F: (f1, f2, fm)

Number of feature sets: N (Training data "train" to learn beta)
Number of new feature sets: q (Test data "test")
What is {g(F) for F in q}?

Step 1: Learn beta from "train"
Step 2: Predict g(F) using learned beta for F in q ("test")
Step 3: Compute Score based on error on "test"
'''

import numpy as np

'''
def estimate_lin_reg(train):
    params = 0
    return params

def predict(test, params):
    y_pred = 0
    return y_pred

def scoring(test, y_pred):
    score = 0
    return score
'''
'''
num = [int(i) for i in input().split()]
m = num[0]
n = num[1]
train = []
for i in range(n):
    line = [float(j) for j in input().split()]
    train.append(line)
q = int(input())
test = []
for i in range(q):
    line = [float(j) for j in input().split()]
    test.append(line)
'''
m, n, q = 2, 3, 1
train = np.matrix([[0, 2, 3],[2, 4, 4],[1, 4, 5]])
test = np.matrix([[4,5,6]])

y = train[:,-1]
x = np.ones(train.shape)
x[:,1:3] = train[:,0:2]
print(x)
print(y)

beta = np.linalg.solve(x, y)
print(beta)

'''
params = estimate_lin_reg(train)
y_pred = predict(test, params)
score = scoring(test, y_pred)
'''