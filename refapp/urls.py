from django.urls import path
from .views import UserRegistration, UserDetails,ReferralsList

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='register'),
    path('details/', UserDetails.as_view(), name='details'),
    path('referrals/', ReferralsList.as_view(), name='referrals-list'),
]
