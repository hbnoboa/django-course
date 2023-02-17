import math

from django.core.paginator import Paginator


def make_pagination_range(
        page_range,
        qty_pages,
        current_page
):
    middle_range = math.ceil(qty_pages / 2)
    start_range = current_page - middle_range
    stop_range = qty_pages + middle_range
    total_pages = len(page_range)

    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    if stop_range >= total_pages:
        start_range = start_range - abs(total_pages - stop_range)

    pagination = page_range[start_range:stop_range]

    return {
        'pagination': pagination,
        'page_range': page_range,
        'qty_pages': qty_pages,
        'current_page': current_page,
        'total_pages': total_pages,
        'start_range': start_range,
        'stop_range': stop_range,
    }


def make_pagination(request, queryset, perpage, qty_pages=5):
    current_page = int(request.GET.get('page', 1))
    previous_page = int(request.GET.get('page', 1))-1
    next_page = int(request.GET.get('page', 1))+1
    paginator = Paginator(queryset, perpage)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        paginator.page_range,
        qty_pages,
        current_page)

    return page_obj, pagination_range, previous_page, next_page
