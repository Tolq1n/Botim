from django.urls import path
from .views.user import UserRetrieveAPIView


urlpatterns = [
    path('<int:pk>', UserRetrieveAPIView.as_view())
]
