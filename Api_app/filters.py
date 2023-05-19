import django_filters
from django.db.models import Count, Q
from django.forms.widgets import TextInput
from django_filters import rest_framework as filters
from django.db.models import F

from Api_app import models
class UserFilter(django_filters.FilterSet):
    Firstname = django_filters.CharFilter(
        label="User Name",
        method="filter_by_name",
    )

    pk = django_filters.CharFilter(
        label="Pk",
        method="filter_by_pk",
    )


    def filter_by_name(self, queryset, name, value):
        if value:
            return models.APi_default.objects.filter(pk=value)
        queryset = models.APi_default.objects.filter(Firstname=value)
        return queryset

    def filter_by_pk(self, queryset, name, value):
        if value:
            return models.APi_default.objects.filter(pk=value)

    class Meta:
        model = models.APi_default
        fields = ["Firstname","id"]

from rest_framework import filters
class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('title_only'):
            return ['title']
        return super().get_search_fields(view, request)




