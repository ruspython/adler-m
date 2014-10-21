from django import template
register = template.Library()
import re


@register.filter(name='site_url')
def site_url(url):
    p = re.compile('^https?://')
    if not p.match(url):
        url = 'http://%s' % url
    return url


@register.filter(name='in_list')
def in_list(value, variants):
    return True if value in variants else False