from django.core.paginator import Paginator
from django.conf import settings


def paginator_func(posts, request):
    paginator = Paginator(posts, settings.POSTS_NUMBER)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)
