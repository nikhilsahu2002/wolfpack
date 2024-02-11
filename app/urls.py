from django.urls import path
from app.views import GetData,postData
from .api import RegisterApi,LoginApi,UserListApi

urlpatterns = [
    path('', GetData),
    path('post/',postData),
    path('api/register/', RegisterApi.as_view()),
    path('api/login/', LoginApi.as_view()),
    path('api/users', UserListApi.as_view()),
]
