---
layout: article
title: 使用markdown书写科技论文
mathjax: true
tags: 写作技巧
comments: true
key: don-kow
# article_header:
#   type: cover
#   image:
#     src: /images/0.jpeg
---


>文本主要讨论如何使用markdown来书写科技论文.

使用markdown书写科技论文的优势和劣势

优势

- 可以使用任何喜欢的编辑器进行书写,并且免费
- 可以借助编辑器的优势,比如说sublime的强大编辑功能/可以随时关闭却不会丢失内容等特性
- markdown学习起来比较简单,源码即时候机器阅读又适合人类阅读
- 文本文件方便和git一起使用,从而得到版本控制的功能,避免了书写过程中想回到一个以前的版本却没有保存的场景(重要)
- 基于github等,方便与他人协作(重要)
- 能够方便使用latex公式,高效地编辑数学公式(其实这是我是用它的一个最主要的原因)
- 方便转换成其他格式

劣势

- 缺少统一和完善的工具链来完成学术写作(相反latex却有)
- 并不是所有人都使用你的工具来进行创作导致与他人协作苦难(相对的)

# 使用 markdown书写科技论文的要求

- 支持公式
- 支持脚注
- 支持引文格式
- 支持图表的自动索引
  
# 看一下整体的效果

<!-- ![](/images/Peek 2018-05-10 12-03.gif) -->

<img src="/images/Peek 2018-05-10 12-03.gif">



# 工具清单
- pandoc
- visual stuido code 
- zotero


# markdown 创作环境

markdown的创作环境可以按照自己的喜好来进行选择，根据本文的经验推荐如下：

- [Visual Studio Code](https://code.visualstudio.com/)
- [Sublime Text](https://www.sublimetext.com/)

使用现代化的代码编辑器的好处在于

- 文档在没有手动保存的情况下，发生突发状况，打开编辑器，所书写的内容依然存在
- 编辑器包含项目浏览器，也支持双排等布局，方便在不同文件之间进行工作
- 编辑器支撑跨文件的搜索，方便快速搜索内容
- 编辑器一般支持第三方插件而且时免费的，可以大大扩展编辑器的功能，也可以自己开发插件，增加自己想要的功能

下面主要以visual studio code为例，来进行说明，如果通过配置一些工具来支撑markdown书写科技论文时的需求。

## markdown 科技论文写作预览

visual studio code 本文所带的 markdown预览不能支持 pandoc markdown的渲染，可以使用 [shd101wyy/markdown-preview-enhanced](https://github.com/shd101wyy/markdown-preview-enhanced) markdown 来进行支撑

安装插件后需要对其进行一些设置，以支撑 pandoc 的参考文献，文档的图标引用等。

## 如何添加引用

利用zotero管理参考文献，并安装插件[betterBibtex](https://github.com/retorquere/zotero-better-bibtex/releases)，利用该插件自动生成bib文件以方面pandoc和visual studio code 使用，也可以直接从zotero里直接copy引用到markdown；

参考文献的格式设置可以通过csl格式文件，结合pandoc进行设置


## 如何添加图片引用

pandoc有一系列的扩展，也支持自定义开发[扩展](https://github.com/jgm/pandoc/wiki/Pandoc-Filters)

[另参见](https://pandoc.org/filters.html)

图片引用支持可以使用[lierdakil/pandoc-crossref](https://github.com/lierdakil/pandoc-crossref)，注意这个扩展的预览速度要快于：

>- https://github.com/tomduck/pandoc-fignos
>- https://github.com/tomduck/pandoc-eqnos
>- https://github.com/tomduck/pandoc-tablenos

预览和编译成 doc文件等，可以参考[这篇](https://sspai.com/post/43471)博客

<img src="/images/2018-10-30-15-04-08.png">

<img src="/images/Peek 2018-05-10 12-03.gif">

# 转换markdown文件到doc文件

>使用pandoc markdown书写markdown文件，这样可以利用pandoc工具，将markdown文件转换成其他格式，比如latex和pdf甚至doc文件(转换PDF需要安装Latex的环境，这里不推荐，可以转换成doc文件再转换成pdf,也可以使用typora导出)。

直接使用命令行


{% highlight shell %}

pandoc -s -f markdown -t docx --filter=c:\\Program Files (x86)\\Pandoc\\pandoc-citeproc --bibliography=C:\\Users\\theki\\Documents\\我的坚果云\\BibtexAndCSL\\my.bib --csl=C:\\Users\\theki\\Documents\\我的坚果云\\BibtexAndCSL\\chinese-gb7714-2005-numeric.csl -o out\\out.docx  output/out.md

{% endhighlight %}

使用[vscode-pandoc - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=DougFinke.vscode-pandoc)

需要进行响应的设置




可以对sublime的build工具进行设置，这样可以自动化的完成pandoc的转化命令

{% highlight python %}
{ 
    "cmd":  ["pandoc", "-s", "-f", "markdown", "-t", "docx", 
    "--filter=/home/kandy/miniconda3/bin/pandoc-citeproc", 
    "--bibliography=/home/kandy/我的坚果云/coWordsStudy/markdownLab/my.bib",
    "--csl=/home/kandy/我的坚果云/coWordsStudy/markdownLab/chinese-gb7714-2005-numeric.csl",
    "-o", "$file_base_name.docx", "$file"],

    "selector": "text.html.markdown"
}

{% endhighlight %}

# 配置文件

参考我的 visual studio code 的[配置文件](/assets/my_settings.json)


# 项目组织和模板

参考我的项目[wybert/AcademicManuscriptMarkdownTemplate](https://github.com/wybert/AcademicManuscriptMarkdownTemplate)



# 参考

[强烈推荐的视频](https://www.youtube.com/watch?v=N31E_NZYQQY&t=175s)


