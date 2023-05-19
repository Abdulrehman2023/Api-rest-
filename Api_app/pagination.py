from rest_framework.pagination import CursorPagination


class CustomPageNumberPagination(CursorPagination):
    page_size = 10
    ordering = 'Email'
   