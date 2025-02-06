from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('api/', include('books.urls')),    # Include books endpoints
    path('api-auth/', include('rest_framework.urls')),  # Enables the login UI
     # Endpoint for clients to obtain a token
    
]
