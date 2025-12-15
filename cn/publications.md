---
layout: post
title: 发表记录
lang: zh
---

## 精选论文
<div class="pubs-list">
{% bibliography --query @*[keywords~=S] %}
</div>

## 期刊文章
<div class="pubs-list">
{% bibliography --query @*[keywords~=J] %}
</div>

## 书籍与章节
<div class="pubs-list">
{% bibliography --query @*[keywords~=B] %}
</div>

{% comment %}
## 会议论文
<div class="pubs-list">
{% bibliography --query @*[keywords~=C] %}
</div>
{% endcomment %}

{% comment %}
## 工作论文
<div class="pubs-list">
{% bibliography --query @*[keywords~=R] %}
</div>
{% endcomment %}

## 演讲
<div class="pubs-list">
{% bibliography --query @*[keywords~=T] %}
</div>

## 海报
<div class="pubs-list">
{% bibliography --query @*[keywords~=P] %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    var publicationContainers = document.querySelectorAll('.pubs-list, .bibliography');
    var myNames = ["Fu, X.", "Xiaokang Fu", "Fu, Xiaokang", "付小康", "Fu†, X.", "Fu†, Xiaokang"]; 

    publicationContainers.forEach(function(container) {
        var entries = container.querySelectorAll('li, p, div.csl-entry');
        entries.forEach(function(entry) {
            var html = entry.innerHTML;
            
            // 1. Cleanup LaTeX dagger variations if any remain
            html = html.replace(/\\dagger/g, '†');
            html = html.replace(/\$\^\\dagger\$\$/g, '†');
            html = html.replace(/\^\\dagger\}/g, '†');
            
            // 2. Bold my name
            myNames.forEach(function(name) {
                if (html.includes(name)) {
                    var regex = new RegExp(name.replace(/[.*+?^${}()|[\\]/g, '\\$&'), 'g');
                    html = html.replace(regex, '<strong>' + name + '</strong>');
                }
            });
            
            entry.innerHTML = html;
        });
    });
});
</script>