from django.contrib.auth.models import User, Group
from rest_framework import  permissions, viewsets

from api.serializers import PostSerializer, UserSerializer, GroupSerializer, TagSerializer, CategorySerializer
from newspaper.models import Post, Tag, Category



class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class TagViewSet(viewsets.ModelViewSet):
    queryset=Tag.objects.all().order_by('name')
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [permissions.AllowAny()]
        
        return super().get_permissions()

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [permissions.AllowAny()]
        
        return super().get_permissions()

class PostViewSet(viewsets.ModelViewSet):
    queryser=Post.objects.all().order_by('-published_at')
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action in ['list','retrieve']:
            queryset= queryset.filter(status="active", published_at__isnull=False)

        return queryset
    
    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [permissions.AllowAny()]
        
        return super().get_permissions()