import numpy as np
import pandas
import math
import matplotlib.pyplot as plt

#Данны точки
E = 10 ** -6

def q(n, x):
    return -(x * x) * (2 * n + 1) / ((n + 1) * (2 * n + 3))

def sum_1(x, E):
    sum_all = 0
    n = 0
    a = x
    while (abs(a) > E):
        sum_all += a
        a = a * q(n, x)
        n = n + 1
    return (sum_all * 2 / pow(np.pi, 0.5))
print(sum_1(0.2, E))
print(sum_1(0.6, E))
print(sum_1(0.8, E))
print()

# задание 1
# Для узлов
def createListOfNodes(a, b, n):

    h = (b - a) / n
    x = []
    for i in range(0, n + 1):
        xi = a + i * h
        x.append(xi)
    return x

def chebListOfNodes(a, b, n):
    x = []
    for i in range(0, n + 1):
        x.append(0.5 * (a + b) + 0.5 * (b - a) * math.cos((2 * i + 1)/(2*n + 2)*math.pi))
        return x

x = createListOfNodes(0, 2, 5)

result_ref = []
for i in range(len(x)):
    result_ref.append(sum_1(x[i], E))

# Для точек
xv = createListOfNodes(0, 2, 10)

def chisl(xv, x, fx):
    sum = 0
    for i in range(len(x)):
        p = 1
        for j in range(len(x)):
            if i != j:
                p *= (xv - x[j]) / (x[i] - x[j])
            sum += p * fx[i]
        return sum

Ln = []
for i in range(len(xv)):
    Ln.append(chisl(xv[i], x, result_ref))

sx = []
for i in range(len(xv)):
    sx.append(sum_1(xv[i], E))

def maxOtvkl(sx, lnx):
    ep = []
    for i in range(len(sx)):
        ep.append(abs(sx[i]-lnx[i]))
    return ep

otkl = maxOtvkl(sx, Ln)
print(otkl)
print()

p = pandas.DataFrame({
    'X~': xv,
    'S(X)': sx,
    'Ln(X)': Ln,
    'S(X)-Ln(X)': otkl})
print(p)

plt.plot(p['X~'], p['S(X)-Ln(X)'])
plt.show()

def maxForNode(start, stop, countOfNodes):
    x = createListOfNodes(start, stop, countOfNodes)
    xv = createListOfNodes(start, stop, countOfNodes * 2)
    result_ref = []
    for i in range(len(x)):
        result_ref.append(sum_1(x[i], E))
    ln = []
    for i in range(len(xv)):
        ln.append(chisl(xv[i], x, result_ref))
    sx = []
    for i in range(len(xv)):
        sx.append(sum_1(xv[i], E))
    return max (maxOtvkl(sx, ln))

def maxForNodeCHeb(start, stop, countOfNodes):
    x = chebListOfNodes(start, stop, countOfNodes)
    xv = createListOfNodes(start, stop, countOfNodes * 2)
    result_ref = []
    for i in range(len(x)):
        result_ref.append(sum_1(x[i], E))

    ln = []
    for i in range(len(xv)):
        ln.append(chisl(xv[i], x, result_ref))
    sx = []
    for i in range(len(xv)):
        sx.append(sum_1(xv[i], E))

    return max (maxOtvkl(sx, ln))

FIRST = 5
LAST = 40
nodesList = []
otklList = []
otklListCheb = []

for i in range(FIRST, LAST):
    nodesList.append(i)
    otklList.append(maxForNode(0,2,i))
    otklListCheb.append(maxForNodeCHeb(0,2,i))

p = pandas.DataFrame({
    'Количество узлов': nodesList,
    'Максимальное отклонение': otklList,
    'Максимальное отклонение с узлами чебышева': otklListCheb
})
print(p)

plt.plot(p['Количество узлов'], p['Максимальное отклонение'])
plt.show()

plt.plot(p['Количество узлов'], p['Максимальное отклонение с узлами чебышева'])
plt.show()