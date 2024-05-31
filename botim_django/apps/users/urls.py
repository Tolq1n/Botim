from django.urls import path
from .views.user import UserRetrieveAPIView, UserListCreateAPIView


urlpatterns = [
    path('<int:pk>', UserRetrieveAPIView.as_view()),
    path('', UserListCreateAPIView.as_view()),
]
