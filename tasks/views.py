from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all().order_by('-id')
  serializer_class = TaskSerializer
  filter_backends = [filters.OrderingFilter]
  ordering_filters = ['name', '-id', 'done']
  ordering = ['-id']
