---
title: 如何组织数据科学项目结构
tags: 项目组织
article_header:
  type: cover
  image:
    src: /images/20140830203351_GdUYR.jpeg
---


> 最近在做一个数据科学项目，总是觉得手头的工具不顺手，代码的结构很混乱，比如
1. 喜欢使用`jupyter notebook`开始一个项目进行数据处理和数据分析，因为它很适合做一些探索性的分析
2. `jupyter notebook`并不包含项目的概念，也没有一个很好的结构来组织这些notebook文件
3. 需要使用使用python脚本的方式执行一些需要大量自动化处理的任务
4. 大量数据无法使用git进行管理，也不需要
5. 项目包含数据以及中间数据使得项目结构混乱
6. 有时候需要制作报告
7. 有时候需要文档记录相关想法
8. 等等


# 使用 cuttercookie datascience 项目结构模板

## 安装 cookiecutter

{% highlight shell %}
pip install --user cookiecutter
{% endhighlight %}

## 根据模板创建项目结构

{% highlight shell %}
cookiecutter https://github.com/drivendata/cookiecutter-data-science
{% endhighlight %}

## 了解项目结构以及如何使用

参考[这个博客](http://drivendata.github.io/cookiecutter-data-science/
)

## 开始自己的项目

记住尽量按照这个标准结构组织文档和代码，但是可是修改子目录结构





