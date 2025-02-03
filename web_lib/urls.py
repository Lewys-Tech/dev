from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('api-auth/', include('rest_framework.urls')),  # Enables the login UI
     # Endpoint for clients to obtain a token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
