from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 20
    # page_query_param = 'my_page'
    page_size_query_param = 'records'
    max_page_size = 7


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10

class MyCursorPagination(CursorPagination):
    page_size = 5
    ordering = 'name'
