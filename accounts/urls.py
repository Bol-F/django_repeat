from django.urls import path

from .views import MeAPIView, RegisterAPIView

urlpatterns = [
    path('me/', MeAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
]