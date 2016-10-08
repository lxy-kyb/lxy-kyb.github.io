title: 关于
summary: 介绍本博客的基本功能
publish_date: 2016-09-15
tags: About
      Markdown

# 关于本文

本博客是本人开发的一个基于Markdown的博客系统，支持基本的Markdown语法及一些常用的扩展语法。本文将对本博客所支持的Markdown语法做介绍。

# Markdown基本语法

Markdown基本语法参见：  
[https://daringfireball.net/projects/markdown/syntax](https://daringfireball.net/projects/markdown/syntax)

# 扩展的Markdown特殊语法

本博客Markdown的生成基于Python的Markdown包，因此本博客支持的扩展语法也源于Python Markdown，参见：[Python Markdown](https://pythonhosted.org/Markdown/)

## META信息的编写方式

META支持作者为Markdown文件添加自定义的一些信息，这些自定义的信息将在页面右侧展示和查看是起作用，目前支持如下信息：

| 关键字       | 含义         |
|:-------------|:-------------|
| title        | 文章标题     |
| summary      | 摘要         |
| publish_date | 文章发布日期 |
| tags         | 标签         |

**注意：**  

 1. 如果`tags`有多个时，请换行书写；
 2. `meta`信息之间不要有空行；
 3. 全部`meta`结尾和正文之间至少保留一个空行；
 4. `meta`信息请使用小写，并使用英文冒号`:`；
 5. `title`如果为填写，则使用`Markdown`文件名作为标题；


例如，本文的Meta信息如下：

	title: 关于
	summary: 介绍本博客的基本功能
	publish_date: 2016-09-15
	tags: About
		  Markdown

## 标题编写
```Markdown
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
```

## 标题编写
```Markdown
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
```


