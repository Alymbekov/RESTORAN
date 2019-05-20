from rest_framework import pagination


class CustomPagination(pagination.LimitOffsetPagination):#PageNumberPagination):
    # page_size = 5
    default_limit = 5
    max_limit = 5
