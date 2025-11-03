from django.urls import path
from .views import TeamListCreate, TeamDetail

urlpatterns = [
    path('', TeamListCreate.as_view(), name='team-list-create'),
    path('<int:pk>/', TeamDetail.as_view(), name='team-detail'),
]
