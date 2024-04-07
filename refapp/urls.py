from django.urls import path
from .views import UserRegistration, UserDetails,ReferralsList

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
]
