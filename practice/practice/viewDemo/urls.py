from django.urls import path
from .views import Index, update_user, home
from .rest_api import List_users, update_user, UserList, UserRetrieveAPIView


urlpatterns = [
    path("", home),
    path("index", Index.as_view()),
    path("update/<id>", update_user),
    path('list', List_users.as_view()),
    path('update/<id>', update_user),
    path('userlist', UserList.as_view()),
    path('userGen/<int:pk>', UserRetrieveAPIView.as_view()),
]