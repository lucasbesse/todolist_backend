from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class TaskViewSet(viewsets.ModelViewSet):
  queryset = Task.objects.all().order_by('-id')
  serializer_class = TaskSerializer
  filter_backends = [filters.OrderingFilter]
  ordering_filters = ['name', '-id', 'done']
  ordering = ['-id']
  permission_classes = [IsAuthenticated]
  
  def get_queryset(self):
     return super().get_queryset().filter(user=self.request.user).order_by('-id')
   
  def perform_create(self, serializer):
     serializer.save(user=self.request.user)
  
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            
            return Response({
              'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
              }
            })
        else:
          return Response(serializer.errors, status=400)
