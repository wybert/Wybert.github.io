---
layout: post
title: Publications
---

## Selected Papers
<div class="pubs-list">
{% bibliography --query @*[keywords~=S] %}
</div>

## Journal Articles
<div class="pubs-list">
{% bibliography --query @*[keywords~=J] %}
</div>

## Books and Chapters
<div class="pubs-list">
{% bibliography --query @*[keywords~=B] %}
</div>

{% comment %}
## Conferences
<div class="pubs-list">
{% bibliography --query @*[keywords~=C] %}
</div>
{% endcomment %}

{% comment %}
## Working Papers
<div class="pubs-list">
{% bibliography --query @*[keywords~=R] %}
</div>
{% endcomment %}

## Talks
<div class="pubs-list">
{% bibliography --query @*[keywords~=T] %}
</div>

## Posters
<div class="pubs-list">
{% bibliography --query @*[keywords~=P] %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    var publicationContainers = document.querySelectorAll('.pubs-list, .bibliography');
    var myNames = ["Fu, X.", "Xiaokang Fu", "Fu, Xiaokang", "Fu†, X.", "Fu†, Xiaokang"]; 

    publicationContainers.forEach(function(container) {
        var entries = container.querySelectorAll('li, p, div.csl-entry');
        entries.forEach(function(entry) {
            var html = entry.innerHTML;
            
            // 1. Cleanup LaTeX dagger variations if any remain
            html = html.replace(/\\dagger/g, '†');
            html = html.replace(/\$\^\\{\\dagger\\}\$/g, '†');
            html = html.replace(/\^\\{\\dagger\}/g, '†');
            
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