from django.contrib.auth.models import User,Group
from rest_framework import serializers
from newspaper.models import Contact, NewsLetter, Post, Tag, Category

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields=["id", "name","icon","description"]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=[
            "id",
            "title",
            "content",
            "featured_image",
            "status",
            "tag",
            "category",
            # read only
            "author",
            "views_count",
            "published_at",
        ]
        extra_kwargs={
            "author":{"read_only":True},
            "views_count":{"read_only":True},
            "published_at":{"read_only":True},
        }

    def validate(self, data):
            data["author"]=self.context["request"].user
            return data
        
class PostPublishSerializer(serializers.Serializer):
    id=serializers.IntegerField()

class NewsletterSerializer(serializers.Serializer):
    class Meta:
        model=NewsLetter
        fields="__all__"
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields="__all__"