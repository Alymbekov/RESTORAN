
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('crm_food.urls')),
    path('auth/', include('users.urls')),
    path('auth/user/', include(('users.user.urls', 'api-user'), namespace='api-user')),

]
