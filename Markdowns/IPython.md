title: IPython入门
summary: IPython入门只是
publish_date: 2017-02-21
tags: python

# IPython: 一个交互式shell工具

### 支持功能
* Tab键自动补全
* 历史记录存档
* 行内编辑
* 使用%run可以调用外部Python脚本
* 支持pylab模式
* Python代码调试和性能分析

### pylab模式
在pylab模式下，IPython将自动导入Scipy，Numpy和Matplotlib模块。
> $ ipython --pylab <br /> 
Python 2.7.2 (default, Jun 20 2012, 16:23:33)<br />
Type "copyright", "credits" or "license" for more information.<br />
<br />
IPython 0.14.dev -- An enhanced Interactive Python.<br />
! -> Introduction and overview of IPython's features.<br />
%quickref -> Quick reference.<br />
help -> Python's own help system.<br />
objec! -> Details about 'object', use 'object??' for extra details.<br />
<br />
Welcome to pylab, a matplotlib-based Python environment [backend: MacOSX].<br />
For more information, type 'help(pylab)'.<br />
In [1]: quit()<br />

### IPython 魔术命令
> %quickref 显示IPython的快速参考<br />
%magic 显示所有魔术命令的详细文档<br />
%debug 从最新的异常跟踪的底部进入交互式调试器<br />
%hist 打印命令的输入（可选输出）历史<br />
%pdb 在异常发生后自动进入调试器<br />
%paste 执行剪贴板中的Python代码<br />
%cpaste 打开一个特殊提示符以便手工粘贴待执行的Python代码<br />
%reset 删除interactive命名空间中的全部变量/名称<br />
%page OBJECT 通过分页器打印输出OBJECT<br />
%run script.py 在IPython中执行一个Python脚本文件<br />
%prun statement 通过cProfile执行statement，并打印分析器的输出结果<br />
%time statement 报告statement的执行时间<br />
%timeit statement 多次执行statement以计算系综平均执行时间。对那些执行时  间非常小的代码很有用<br />
%who、%who_ls、%whos 显示interactive命名空间中定义的变量，信息级别/冗余度可变<br />
%xdel variable 删除variable，并尝试清除其在IPython中的对象上的一切引用<br />

### IPython 系统交互命令
>%alias ll ls -l 将ll作为ls -l的别名暂时保存<br />
%!cmd 在系统shell中执行cmd<br />
%output  = !cmd args 执行cmd，并将stdout存放在output中<br />
%alias alias_name cmd 为系统shell命令定义别名<br />
%bookmark 使用IPython的目录书签系统<br />
%cd directory 将系统工作目录更改为directory<br />
%pwd 返回系统的当前工作目录<br />
%pushd directory 将目前目录入栈，并转向目标目录<br />
%popd 弹出栈顶目录，并转向该目录<br />
%dirs 返回一个含有当前目录栈的列表<br />
%dhist 打印目录访问历史<br />
%env 以dict形式返回系统环境变量<br />