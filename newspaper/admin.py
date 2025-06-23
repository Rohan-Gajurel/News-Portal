from django.contrib import admin
from newspaper.models import Category, NewsLetter,Post,Tag,Advertisment, UserProfile, Comment, Contact

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertisment)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Contact)
