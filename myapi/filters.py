from django.utils import timezone
from django_filters import DateFilter
from django_filters.rest_framework import FilterSet

from myapp.myapp.models import Uni


class UniFilter(FilterSet):
    upload_date = DateFilter(field_name="created_at", lookup_expr="date")

    class Meta:
        model = Menu
        fields = ["upload_date"]

    @property
    def qs(self):
        queryset = super().qs
        query_params = getattr(self.request, "query_params", {})
        if "upload_date" not in query_params.keys():
            queryset = queryset.filter(created_at__date=timezone.now().date())
        return queryset