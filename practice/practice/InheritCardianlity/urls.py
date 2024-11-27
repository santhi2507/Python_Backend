from django.urls import path
from InheritCardianlity.views import UserListCreateAPIView


urlpatterns = [
    path('', UserListCreateAPIView.as_view()),
]