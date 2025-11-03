from django.urls import path
from .views import BlogListCreate, BlogDetail

urlpatterns = [
    path('', BlogListCreate.as_view(), name='blog-list-create'),
    path('<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
]
