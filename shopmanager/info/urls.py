from django.urls import path, include
from .views import InfoListView, InfoDetailView


urlpatterns = [
    path('', InfoListView.as_view(), name='info'),
    path('info-detail/<int:pk>/', InfoDetailView.as_view(), name='info_detail'),
]