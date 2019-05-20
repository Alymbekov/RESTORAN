from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import UserDeatilAPIView
    # , UserStatusAPIView

urlpatterns = [
    path('<username>/', UserDeatilAPIView.as_view(), name='user-detail'),
    # path('<username>/status/', UserStatusAPIView.as_view(), name='user-status'),
]
