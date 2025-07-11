from django.urls import path
from newspaper import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("post-list/",views.PostListView.as_view(),name="post-list"),
    path("post-detail/<int:pk>", views.PostDetailView.as_view() ,name="post-detail"),
    path("comment/", views.CommentView.as_view(), name="comment"),
    path("post-by-category/<int:category_id>/",views.PostByCategoryView.as_view(), name="post-by-category"),
    path("categories/", views.CategoryListView.as_view(), name="categories"),
    path("tags/", views.TagListView.as_view(), name="tags"),
    path("post-by-tag/<int:tag_id>/", views.PostByTagView.as_view(), name="post-by-tag"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("newsletter/", views.NewsLetterView.as_view(), name="newsletter"),
    path("search/", views.PostSearchView.as_view(), name="search"),
]