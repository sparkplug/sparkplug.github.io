---
layout: blog
title: Insights
permalink: /blog/
---
<div id="content">
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        {% for post in site.posts %}
        <div class="post type-post format-standard status-publish hentry">
          <h2 class="entry-title"><a href="{{ post.url }}" rel="bookmark" title="{{ post.title }}">{{ post.title }}</a></h2>
          <div class="entry-meta entry-header">
            <span class="author">{{ post.author }}</span> .
            <span class="published">{{ post.date | date: "%b %-d, %Y" }}</span>
          </div>
          <div class="entry-content">
            {% if post.summary %}
              {{ post.summary }}
            {% else %}
              {{ post.excerpt }}
            {% endif %}
         </div>
         <a class="read-more" href="{{ post.url }}">Continue reading.. </a> 
       </div>
       {% endfor %}
     </div> 
   </div>
  </div>
</div>

