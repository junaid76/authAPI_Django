from django.urls import path
from .views import RegistrationAPIView,LoginAPIView,LogoutAPIView,HomeAPIView

urlpatterns=[
    path('',HomeAPIView.as_view(),name='home'),
    path('register/',RegistrationAPIView.as_view(),name='register'),
    path('login/',LoginAPIView.as_view(),name='login'),
    path('logout/',LogoutAPIView.as_view(),name='logout'),
]