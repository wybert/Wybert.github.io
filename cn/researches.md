---
layout: default
lang: zh
---

<!-- add google search meta description -->

<meta
    name="description"
    content="我的研究兴趣包括地统计学与地理信息科学（GIS）、城市计算、社交媒体数据挖掘和应急响应。"
/>

<h1>我的研究</h1>

<h2>研究项目</h2>

{% include card_list.html collection=site.data.research_cn.project_entries %}

<h2>开源工具</h2>

{% include card_list.html collection=site.data.research_cn.old_project_entries %}
