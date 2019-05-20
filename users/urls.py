from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import AuthAPIView, RegisterAPIView, UserViewList

urlpatterns = [
    path('', AuthAPIView.as_view(), name='auth'),
    # path('', UserViewList.as_view(), name='auth'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('jwt/', obtain_jwt_token),
    # path('logout/', Logout.as_view(), name='logout'),
    path('jwt/refresh/', refresh_jwt_token),
    path('rest-auth/', include('rest_auth.urls')),
]
