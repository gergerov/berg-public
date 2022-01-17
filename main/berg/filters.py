from rest_framework import filters


class ProductFilter(filters.SearchFilter):
  search_title = 'Поиск продуктов'
  search_description = 'Поиск продуктов по их названиям'
