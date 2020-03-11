from django.urls import path
from .views import PostAPIView, TechCicadaByAnandBoreda

urlpatterns = [
    path('', TechCicadaByAnandBoreda.as_view(), name='api_detail'),
    path('<int:pk>', PostAPIView.as_view(), name='list'),
]