from django.urls import path
from .views import MovieAPIView, MovieDetail

urlpatterns = [
    path('', MovieAPIView.as_view()),
    path('<int:pk>/', MovieDetail.as_view())
]