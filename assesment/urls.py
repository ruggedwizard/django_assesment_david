from django.contrib import admin
from django.urls import path, include

"""JWT_AUTH_URL IMPORTS """
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls'))
]

"""JWT AUTH URL"""
urlpatterns +=[
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist')
]