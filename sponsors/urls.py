from django.urls import path
from .views import SponsorListCreate, SponsorDetail

urlpatterns = [
    path('', SponsorListCreate.as_view(), name='sponsor-list-create'),
    path('<int:pk>/', SponsorDetail.as_view(), name='sponsor-detail'),
]
