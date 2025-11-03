from django.urls import path
from .views import SettingsView, ArsivEntryListView

urlpatterns = [
    path('settings/', SettingsView.as_view(), name='settings'),
    path('', ArsivEntryListView.as_view(), name='arsiv-list'),
]
