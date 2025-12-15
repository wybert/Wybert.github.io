---
layout: home_cn
lang: zh
permalink: /cn/
---

<!-- add google search meta description -->

<meta
    name="description"
    content="付小康的个人网站。付小康是武汉大学测绘遥感信息工程国家重点实验室的博士后研究员，也是哈佛大学地理分析中心（CGA）的访问学者。他也是空间搜搜人（Spatial Search People）的执行人。他的研究兴趣包括地统计学与地理信息科学（GIS）、城市计算、社交媒体数据挖掘和应急响应。"
/>

<!-- <h1>{{ site.title }}</h1> -->
{% if site.theme_config.show_description == true %}
{% include profile_header_cn.html %}
{% endif %} {% if site.theme_config.show_projects == true %}
<h2>精选研究</h2>
{% include card_list.html collection=site.data.home_cn.project_entries %} {% endif
%}

<h2>发表记录</h2>

<div class="pubs-list">
{% bibliography --query @*[keywords~=S] %}
</div>
{% include bold_author_script.html %}

<p><a href="https://wybert.github.io/cn/publications">阅读更多...</a></p>

{% if site.theme_config.show_misc_list == true %}
<h2>{{ site.theme_config.home.title_misc_list }}</h2>
{% include vertical_list.html collection=site.data.home_cn.misc_entries %} {% endif
%} {% if site.theme_config.show_blog == true %}
<h2>{{ site.theme_config.home.title_blog }}</h2>
{% include post_list.html %} {% endif %} {% if
site.theme_config.show_old_projects == true %}
<h2>{{ site.theme_config.home.title_old_projects }}</h2>
{% include card_list.html collection=site.data.home_cn.old_project_entries %} {%
endif %}

<h2>GitHub 统计</h2>
<picture style="display: block; text-align: left;">
    <source
        srcset="https://github-readme-stats.vercel.app/api?username=wybert&show_icons=true&theme=dark"
        media="(prefers-color-scheme: dark)"
    />
    <source
        srcset="https://github-readme-stats.vercel.app/api?username=wybert&show_icons=true&theme=default"
        media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)"
    />
    <img src="https://github-readme-stats.vercel.app/api?username=wybert&show_icons=true&theme=default" alt="Wybert's GitHub stats" style="margin: 0;"/>
</picture>
<br clear="all">

<!-- show services -->
<h2>服务</h2>
<!-- show my services as ceo of ssp -->
<p>
    作为<a href="https://luojiassp.github.io/">空间搜搜人 (SSP)</a> 的执行人。SSP 是一个由来自世界各地的学者组成的非营利科学社区。我们目前的工作主要集中在中文微博数据的情感提取和挖掘。我们也对空间搜索和空间数据挖掘在社交媒体中的应用感兴趣。
</p>
<br />
<a href="https://wybert.github.io/cn/services/">阅读更多...</a>

{% if site.theme_config.show_footer == true %}
<footer>
    <div class="dashed"></div>
    {% include horizontal_list.html collection=site.data.home_cn.footer_entries %}
</footer>
{% endif %}
