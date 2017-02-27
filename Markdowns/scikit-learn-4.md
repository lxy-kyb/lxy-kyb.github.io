title: scikit-learn（四） sklearn常用属性与功能
summary: sklearn常用属性与功能
tags: Machine-Learning

# sklearn常用属性与功能
***

这里还是以`LinearRegression`为例，首先导入包，数据，还有模型。
```python
from sklearn import datasets
from sklearn.linear_model import LinearRegression

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

model = LinearRegression()
```
***
接下来`model.fit`和`model.predict`就属于Model的功能，用来训练模型，并用训练好的模型预测
```python
model.fit(data_X,data_y)

print model.predict(data_X[:4,:])
```
***
> [ 30.00821269  25.0298606   30.5702317   28.60814055]  
***
然后，`model.coef_` 和 `model.intercept_`属于Model的属性，例如对于`LinearRegression`这个模型，这两个属性
分别输出模型的斜率和截距。
```python
print model.coef_
print model.intercept_
```
***

> [ -1.07170557e-01   4.63952195e-02   2.08602395e-02   2.68856140e+00  
  -1.77957587e+01   3.80475246e+00   7.51061703e-04  -1.47575880e+00  
   3.05655038e-01  -1.23293463e-02  -9.53463555e-01   9.39251272e-03  
  -5.25466633e-01]  
36.4911032804

***

`model.get_params()`，用来取出之前定义的参数。
```python
print model.get_params()
```
***
>{'copy_X': True, 'normalize': False, 'n_jobs': 1, 'fit_intercept': True}

***
`model.score(data_X, data_y)` 可以对Model使用`R^2`的方式进行打分，输出精确度。
关于`R^2 coefficient of determination`可以查看[wiki](https://en.wikipedia.org/wiki/Coefficient_of_determination)
```python
print model.score(data_X, data_y)
```
***
> 0.740607742865
***

[查看全部代码](https://github.com/lxy-kyb/scikit-learn-tutorial/blob/master/model_try.py)