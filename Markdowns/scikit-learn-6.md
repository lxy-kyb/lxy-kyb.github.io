title: scikit-learn（六） 交叉验证 Cross-validation（1）
summary: sklearn 交叉验证
tags: Machine-Learning

# 交叉验证 Cross-validation（1）
***
Sklearn中的Cross Validation 对于我们选择正确的Model和Model的参数是非常有帮助的，
我们能只管的看出不同Model或者参数对于结构准确度的影响。

### 1. 基础验证方法
```python
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier #K近邻分类

#加载iris数据集
iris = load_iris()
X = iris.data
y = iris.target

#分割数据集 random_state 为随机数种子保证每次分割的数据一致
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 4)

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)

print knn.score(X_test, y_test)
```
***
> 0.973684210526
***

### 2. 交叉验证法
```python
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier #K近邻分类

#加载iris数据集
iris = load_iris()
X = iris.data
y = iris.target

knn = KNeighborsClassifier()

scores = cross_val_score(knn, X, y, cv = 5, scoring='accuracy')

print scores
print scores.mean()
```
***
>  [ 0.96666667  1.          0.93333333  0.96666667  1.        ]  
0.973333333333
***

### 3. 如何选择模型参数 -- accuray

一般来说`准确率（accuracy）`可以用于判断`分类（Classification）`模型的好坏。
```python
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier #K近邻分类
import matplotlib.pyplot as plt

#加载iris数据集

iris = load_iris()
X = iris.data
y = iris.target

k_range = range(1, 31)
k_scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv = 10, scoring = 'accuracy')
    k_scores.append(scores.mean())

plt.plot(k_range, k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Vlidated Accurcy')
plt.show()
```
***
![datasets](../static/images/machine-learning/f6_1.png)
***
从图中可以得知，`k`值的选择在`12~18`最好。高过`18`以后，准确率开始下降。
下降的原因就是`过拟合（Over fitting）`问题

### 4. 如何选择模型参数 -- Mean squared error
一般来说`平均方差(Mean squared error)`可以用于判断`回归（Regression）`模型的好坏。
```python
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier #K近邻分类
import matplotlib.pyplot as plt

#加载iris数据集
iris = load_iris()
X = iris.data
y = iris.target

k_range = range(1, 31)
k_scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    loss = -cross_val_score(knn, X, y, cv=10, scoring='mean_squared_error')
    k_scores.append(loss.mean())

plt.plot(k_range, k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Vlidated MSE')
plt.show()
```
***
![datasets](../static/images/machine-learning/f6_2.png)
***
由此图可以得知，平均方差越低越好，因此选择`13~18`左右`K`值最好。

[查看全部代码](https://github.com/lxy-kyb/scikit-learn-tutorial/blob/master/cross-validation-1.py)