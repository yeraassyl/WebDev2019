from django_filters import rest_framework as filters
from api.models import Task



class TaskFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Task
        fields = ('id', 'name', 'status', 'task_list_id')