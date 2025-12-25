from django.contrib import admin
from newspaper.models import Category, NewsLetter, Post, Tag, Advertisment, UserProfile, Comment, Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertisment)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(NewsLetter)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

# Register Post after defining PostAdmin
admin.site.register(Post, PostAdmin)
