from django import template
from ..models import BlogTag, Blog
import datetime
import math

register = template.Library()


@register.inclusion_tag('blog/blog_tag_list.html')
def blog_tag_list():
    tags = list(set(BlogTag.objects.all()))
    for article in Blog.objects.all():
        for tag in article.get_all_tags():
            if not tag in tags:
                tags.append(tag)
    return {
        'tags': tags,
    }


@register.inclusion_tag('blog/blog_archive.html')
def blog_archive():
    m_list = []

    def add2m_list(dt):
        ndt = datetime.datetime(dt.year, dt.month, 1)
        if ndt not in m_list:
            m_list.append(ndt)

    for m in Blog.objects.values_list('date'):
        add2m_list(m[0])

    cs = int(math.ceil(len(m_list) / 2))
    m_lists = [
        m_list[:cs],
        m_list[cs:],
    ]

    return {
        'month_lists': m_lists
    }
