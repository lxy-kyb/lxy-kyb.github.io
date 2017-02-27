title: scikit-learn（二） 通用学习模式
summary: scikit-learn通用的学习模式
tags: Machine-Learning

Sklearn 把所有机器学习的模式整合统一起来了，学会一个模式就可以通吃其他不同类型的学习模式。

今天 用 `KNN classifier` 作为样例

Sklearn 包含了许多数据库可以用来练习。以Iris的数据为例，这种花有四个属性，花瓣的长宽，茎的长宽，根据这些属性把花分为三类。

接下来，我们要用分类器取把花按类型分开。

## 使用模型的步骤
1. 导入模块
2. 创建数据
3. 建立模型 - 训练 - 预测

### 导入模块
```python
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
```

### 创建数据
加载`iris`的数据，把属性存在`iris_X`，类别标签存储在`iris_Y`
```python
iris = datasets.load_iris()
iris_X = iris.data
iris_Y = iris.target
```

观察一下数据集，`iris_X`有四个属性，`iris_Y`有0，1，2三类
```python
print iris_X[:2,:]
print (iris_Y)
``` 

> [[ 5.1  3.5  1.4  0.2]  
 [ 4.9  3.   1.4  0.2]]  
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
 2 2]

 把数据集分为训练集和测试集，其中`test_size = 0.3`, 即测试集占总数据的30%
 ```python
 X_train, X_test, y_train, y_test = train_test_split(
     iris_X,iris_Y,test_size = 0.3)
 ```

输出分开后的数据集，顺序也被打乱，更有利于学习模型
```python
print ((y_test))
```
> [1 2 2 1 1 1 0 0 0 2 2 1 2 1 2 0 1 0 2 0 0 1 0 0 0 2 0 1 2 1 0 2 0 2 0 2 1
 0 1 0 0 1 0 0 0 1 0 0 1 2 2 0 2 2 0 2 0 1 2 1 1 0 0 2 1 1 0 0 0 1 1 1 1 2
 2 2 2 1 1 2 1 2 0 2 0 2 2 1 2 0 1 2 1 1 1 1 2 2 1 2 0 0 2 0 2]

 ### 定义模型 - 训练模型 - 预测
 
 定义模块方式为`KNeighborsClassifier()`, 用`fit`来训练`training data`，这一步就
 完成了训练的所有步骤，后面的 `knn`就已经是训练好的模型，就可以直接用来`predict`测试集
 的数据。
 ```python
knn = KNeighborsClassifier()
knn.fit(X_train,y_train)
 ```
 对比用模型预测的值与真实的值，可以看出大概模拟出了数据，有些许的误差
 ```python
 print knn.predict(X_test)
 print y_test
 ```
 > [0 1 1 1 2 2 0 1 0 0 1 0 0 2 2 2 2 0 2 1 2 0 1 1 1 0 2 2 2 1 1 0 0 0 2 2 2
 1 0 2 0 2 0 1 1]  
[0 1 1 1 1 2 0 1 0 0 1 0 0 2 2 2 1 0 2 1 2 0 1 1 1 0 2 2 2 1 1 0 0 0 2 2 2
 1 0 2 0 2 0 1 1]

#### [查看本文全部代码](https://github.com/lxy-kyb/scikit-learn-tutorial/blob/master/knn_try.py)