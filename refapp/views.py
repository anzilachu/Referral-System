from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import CustomUser
from .serializers import UserSerializer, UserRegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination



class UserRegistration(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)  # Generate token
            return Response({'id': user.id, 'token': token.key, 'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
class UserDetails(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    

class CustomPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ReferralsList(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get(self, request):
        current_user = request.user  # Get the current authenticated user
        referral_code = current_user.referral_code

        if not referral_code:
            return Response({'message': 'No referral code found for the current user'}, status=status.HTTP_400_BAD_REQUEST)

        referred_users = CustomUser.objects.filter(referral_code=referral_code)

        # Apply pagination
        paginator = self.pagination_class()
        paginated_users = paginator.paginate_queryset(referred_users, request)

        serializer = UserSerializer(paginated_users, many=True)
        # Extract timestamp of registration for each referral
        referrals_with_timestamp = []
        for referral in serializer.data:
            user_id = referral['id']
            timestamp = CustomUser.objects.get(id=user_id).date_joined
            referral['timestamp_of_registration'] = timestamp
            referrals_with_timestamp.append(referral)

        return paginator.get_paginated_response(referrals_with_timestamp)




