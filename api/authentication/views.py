from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import UserSignUpSerializer, UserProfileSerializer, UserUpdateSerializer
from authentication.models import User, UserProfile
from .permissions import IsAnonymousUser

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserSignUpView(APIView):
    """View For User Registration"""

    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')

        print(request.data)

        if (not first_name or not last_name or not email):
            return Response({'detail': 'All The Fields Are Required'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserSignUpSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                # user.set_password
                print(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class UserUpdateProfile(APIView):
    """View for user to update their profile"""

    queryset = UserProfile.objects.all()
    serializer_class = UserSignUpSerializer

    permission_classes = [IsAuthenticated]

    def get(self, request):
        # user = UserProfile.objects.get(pk= pk)
        serializer = UserUpdateSerializer(request.user, context={'request': request})
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        serializer = UserUpdateSerializer(request.user, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

