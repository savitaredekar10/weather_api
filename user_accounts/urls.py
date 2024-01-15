from django.urls import path
from .views import register_user
from .views import CustomTokenObtainPairView
from .views import secure_endpoint

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('secure/', secure_endpoint, name='secure_endpoint'),
]
