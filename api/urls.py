from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'newsletters', views.NewsletterViewSet)
router.register(r'contacts', views.ContactViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path(
        "post-by-category/<int:category_id>/", views.PostListByCategory.as_view(),
        name="post-list-by-category-api"
    ),
    path(
        "post-by-tag/<int:tag_id>/",
        views.PostListByTag.as_view(),
        name="post-list-by-tag"
    ),
    path(
        "draft-list",
        views.DraftListView.as_view(),
        name="draft-list-api",
    ),
    path("draft-detail/<int:pk>/",
    views.DraftDetailView.as_view(),
    name="draft-detail-api"  
         ),
    path(
        "post-publish",
        views.PostPublishedView.as_view(),
        name="draft-published-api"
    ),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]