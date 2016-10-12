title: Python Data Structure Chapter 1： Lists
summary: Python Lists详解
tags: Python
      Data Structure

# Python Lists
### Lists 初始化
```Python
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]
```

### 获取Lists中的数据

**Code**

```Python
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
``` 	

**result：**

	list1[0]:  physics
	list2[1:5]:  [2, 3, 4, 5]

### 更新Lists中的数据

**Code**

```Python
list = ['physics', 'chemistry', 1997, 2000];

print "Value available at index 2 : "
print list[2]
list[2] = 2001;
print "New value available at index 2 : "
print list[2]
``` 	

**result：**

	Value available at index 2 :
	1997
	New value available at index 2 :
	2001
	
### 删除Lists中的数据

**Code**

```Python
list1 = ['physics', 'chemistry', 1997, 2000];

print list1
del list1[2];
print "After deleting value at index 2 : "
print list1
``` 	

**result：**

	 ['physics', 'chemistry', 1997, 2000]
	 After deleting value at index 2 :
	 ['physics', 'chemistry', 2000]


	
### Lists 基本运算
| Python Expression            | Result                       | Description                |
|:-----------------------------|:-----------------------------|----------------------------|
| len([1, 2, 3])               | 3                            | 获取Lists长度              |
| [1, 2, 3] + [4, 5, 6]        | [1, 2, 3, 4, 5, 6]           | Lists的拼接                |
| ['Hi!'] * 4                  | ['Hi!', 'Hi!', 'Hi!', 'Hi!'] | 元素的repetition           |
| 3 in [1, 2, 3]               | True                         | 判断元素是否存在与Lists中  |
| for x in [1, 2, 3]: print x, | 1 2 3                        | 迭代遍历                   |

### Lists 索引、切割
假设初始化一个Lists如下
```Python
L = ['spam', 'Spam', 'SPAM!']
``` 	

**Table：**

| Python Expression            | Result                       | Description                    |
|:-----------------------------|:-----------------------------|--------------------------------|
| L[2]                         | 'SPAM!'                      | Offsets start at zero          |
| L[-2]                        | 'Spam'                       | Negative: count from the right |
| L[1:]                        | ['Spam', 'SPAM!']            |	Slicing fetches sections       |

### Python includes the following list functions
**1.len(list)**

Parameters

* list -- This is a list for which number of elements to be counted.

Return Value -- his method returns the number of elements in the list.
  
Example Code
```Python
list1, list2 = [123, 'xyz', 'zara'], [456, 'abc']

print "First list length : ", len(list1)
print "Second list length : ", len(list2)
```

Result

	First list length :  3
	Second list length :  2

**2.max(list)**

Parameters

* list -- This is a list from which max valued element to be returned.

Return Value -- This method returns the elements from the list with maximum value.
  
Example Code
```Python
list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]

print "Max value element : ", max(list1)
print "Max value element : ", max(list2)
```

Result

	Max value element :  zara
	Max value element :  700

**3.min(list)**

Parameters

* list -- This is a list from which min valued element to be returned.

Return Value -- This method returns the elements from the list with minimum value.
  
Example Code
```Python
list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]

print "min value element : ", min(list1)
print "min value element : ", min(list2)
```

Result

	min value element :  123
	min value element :  200
	
**4.list(seq)**

Parameters

* seq -- 需要转化为Lists的元组

Return Value -- This method returns the list
  
Example Code
```Python
aTuple = (123, 'xyz', 'zara', 'abc');
aList = list(aTuple)

print "List elements : ", aList
```

Result

	List elements :  [123, 'xyz', 'zara', 'abc']
	
### Python includes following list methods
**1.list.append(obj)**

Parameters

* obj -- This is the object to be appended in the list.

Return Value -- This method does not return any value but updates existing list.
  
Example Code
```Python
aList = [123, 'xyz', 'zara', 'abc'];
aList.append( 2009 );
print "Updated List : ", aList
```

Result

	Updated List :  [123, 'xyz', 'zara', 'abc', 2009]

**2.list.count(obj)**

Parameters

* obj -- This is the object to be counted in the list.

Return Value -- This method returns count of how many times obj occurs in list.
  
Example Code
```Python
aList = [123, 'xyz', 'zara', 'abc', 123];

print "Count for 123 : ", aList.count(123)
print "Count for zara : ", aList.count('zara')
```

Result

	Count for 123 :  2
	Count for zara :  1

**3.list.extend(seq)**

Parameters

* seq -- This is the list of elements

Return Value -- This method does not return any value but add the content to existing list.
  
Example Code
```Python
aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)

print "Extended List : ", aList 
```

Result

	Extended List :  [123, 'xyz', 'zara', 'abc', 123, 2009, 'manni']
	
**4.list.index(obj)**

Parameters

* obj -- This is the object to be find out.

Return Value -- This method returns index of the found object otherwise raise an exception indicating that value does not find.
  
Example Code
```Python
aList = [123, 'xyz', 'zara', 'abc'];

print "Index for xyz : ", aList.index( 'xyz' ) 
print "Index for zara : ", aList.index( 'zara' ) 
```

Result

	Index for xyz :  1
	Index for zara :  2
	
**5.list.insert(index, obj)**

Parameters

* index -- This is the Index where the object obj need to be inserted.
* obj -- This is the Object to be inserted into the given list.

Return Value -- This method does not return any value but it inserts the given element at the given index.

Example Code
```Python
aList = [123, 'xyz', 'zara', 'abc']

aList.insert( 3, 2009)

print "Final List : ", aList
```

Result

	Final List : [123, 'xyz', 'zara', 2009, 'abc']
	
**6.list.pop(obj=list[-1])**

Parameters

* obj -- This is an optional parameter, index of the object to be removed from the list.
  
Return Value -- This method returns the removed object from the list.

Example Code
```Python
aList = [123, 'xyz', 'zara', 'abc'];

print "A List : ", aList.pop()
print "B List : ", aList.pop(2)
```

Result

	A List :  abc
	B List :  zara
	
**7.list.remove(obj)**

Parameters

* obj -- This is the object to be removed from the list.
  
Return Value -- This method does not return any value but removes the given object from the list.

Example Code
```Python
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.remove('xyz');
print "List : ", aList
aList.remove('abc');
print "List : ", aList
```

Result

	List :  [123, 'zara', 'abc', 'xyz']
	List :  [123, 'zara', 'xyz']
	
**8.list.reverse()**

Parameters

* NA
  
Return Value -- This method does not return any value but reverse the given object from the list.

Example Code
```Python
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.reverse();
print "List : ", aList
```

Result

	List :  ['xyz', 'abc', 'zara', 'xyz', 123]
	
**9.list.sort([func])**

Parameters

* NA
  
Return Value -- This method does not return any value but reverse the given object from the list.

Example Code
```Python
aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.sort();
print "List : ", aList
```

Result

	List :  [123, 'abc', 'xyz', 'xyz', 'zara']