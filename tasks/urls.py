from django.urls import path, include
from rest_framework .routers import DefaultRouter
from .views import TaskViewSet, RegisterView, LoginView
from rest_framework.authtoken.views import obtain_auth_token

#{"token":"a1fdafc8499ac09b85b1fe3f19cead8fd8cdc138"}
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/', include(router.urls)),
]