title: Python文件操作
summary: Python文件操作详解
tags: Python
      FILE IO

# Python文件操作
### 创建文件
```Python
import os
os.mknod("test.txt")        #创建空文件
fp = open("test.txt",w)     #直接打开一个文件，如果文件不存在则创建文件
```

### open的模式
* w      以写方式打开，
* a      以追加模式打开 (从 EOF 开始, 必要时创建新文件)
* r+     以读写模式打开
* w+     以读写模式打开 (参见 w )
* a+     以读写模式打开 (参见 a )
* rb     以二进制读模式打开
* wb     以二进制写模式打开 (参见 w )
* ab     以二进制追加模式打开 (参见 a )
* rb+    以二进制读写模式打开 (参见 r+ )
* wb+    以二进制读写模式打开 (参见 w+ )
* ab+    以二进制读写模式打开 (参见 a+ )

### 路径操作：判断获取和删除
1.得到当前工作目录，即当前Python脚本工作的路径
```Python
currentpath = os.getcwd()
```

2.返回指定目录下的所有文件和目录名
```Python
list_file = os.listdir('f:/Python')             # os.listdir('~/Python')
```

3.判断给出的路径是否存在
```Python
if os.path.exists(path):
	print path, 'exist'
else:
	print path, 'not exist'
```

4.判断给出的路径是否是一个文件
```Python
if os.path.isfile(path):
	print path, 'is a file'
else:
	print path, 'not a file'
```

5.判断给出的路径是否是一个目录
```Python
if os.path.isdir(path):
	print path, 'is a directory'
else:
	print path, 'not a directory'
```

6.判断给出的路径是否是绝对路径
```Python
if os.path.isabs(path):
	print path, 'is a absolutly directory'
else:
	print path, 'not a absolutly directory'
```

7.返回一个路径的目录名和文件名
```Python
print os.path.split('D:\hello\json.txt')        #('D:\\hello', 'json.txt') 
print os.path.split('/home/Python/test.py')     #('/home/Python', 'test.py')
```

8.获得路径名
```Python
print os.path.dirname('D:\hello\json.txt')      #'D:\\hello'
print os.path.dirname('/home/Python/test.py')   #'/home/Python'
```

9.获得文件名
```Python
print os.path.basename('D:\hello\json.txt')     #'json.txt'
print os.path.basename('/home/Python/test.py')  #'test.py'
```

10.分离文件扩展名
```Python
print os.path.splitext('D:\hello\json.txt')     #('D:\\hello\\json', '.txt') 
print os.path.splitext('/home/Python/test.py')  #('/home/Python/test', '.py')
```

11.进入目录
```Python
os.chdir
```

12.创建目录
```Python
os.mkdir('test')          #创建单个目录
os.mkdirs('Python/test')  #创建多级目录
```

###文件操作
1.复制文件（目录）
```Python
shutil.copyfile('old', 'new')      #old和new都只能是文件
shutil.copy('old', 'new')          #old只能是文件夹，new可以是文件也可以是目标目录
shutil.copytree('olddir','newdir') #olddir和newdir只能是目录，且newdir不存在
```

2.重命名文件（目录）
```Python
os.rename('oldname','newname')     #文件或目录都是使用这条命令
```

3.移动文件（目录）
```Python
shutil.move('old','new')   		   #文件或目录都是使用这条命令
```

4.删除文件（目录）
```Python
os.remove('file')
os.rmdir('dir')                    #只能删除空目录
shutil.rmtree('dir')               #空目录、有内容的目录都可以删
```