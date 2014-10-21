from django import template

register = template.Library()

@register.inclusion_tag('pagination/pagination.html', takes_context=True)
def pagination(context, extra_pages=3):
    try:
        page_list = context["page_obj"].paginator.page_range
        current_page = context["page_obj"].number
        current_page_index = current_page - 1
        page_len = len(page_list)
        list_start = current_page_index - extra_pages
        if list_start < 0:
            list_start = 0
        list_end = current_page_index + extra_pages + 1
        if list_end > page_len:
            list_end = page_len

        def page_url_create(p):
            request = context['request']
            get_params = request.GET.copy()
            get_params['page'] = p
            return '%s?%s' % (request.path, get_params.urlencode())

        def create_page(p):
            if p in page_list:
                return {
                    'text': p,
                    'url': page_url_create(p),
                    'is_current': p == current_page
                }
            else:
                return None

        visible_pages = [create_page(page) for page in page_list[list_start:list_end]]
        return {
            "is_paginated": context["is_paginated"],
            "page_obj": context["page_obj"],
            'visible_pages': visible_pages,
            'prev_page': create_page(current_page-1),
            'next_page': create_page(current_page+1),
            'first_page': create_page(1),
            'last_page': create_page(page_len),
            'get_params': [(k, v) for k, v in context['request'].GET.copy().items() if v],
        }
    except KeyError:
        return {
            "is_paginated": False
        }