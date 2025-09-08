from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer, LoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# Create your views here.
class RegisterView(APIView):
    # *** allow unauthenticated access to endpoint
    permission_classes = [AllowAny]

    def post(self, request):
    # attach incoming JSON data to a serializer
        serializer = UserRegistrationSerializer(data=request.data)
        #   validate data
        if serializer.is_valid():
            user = serializer.save()
            # fetch user token(created during registration)
            token = Token.objects.get(user=user)
            #Formula: return Response(<dict>, status=<status_code>)
            # send respond back as JSON with given HTTP status
            return Response(
                {
                    'message': 'User registered successfully!', #success message
                    # convert user object into JSON-safe data
                    'user': UserRegistrationSerializer(user).data,
                    'token': token.key
                }, status=status.HTTP_201_CREATED)
        # Formula: return Response(serializer.errors, status=400)
        # show error message if validation fails
        return Response(
            {
                'message': 'Registration failed!'
                'error': serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    # allow all users to login
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
        # run against database check to confirm user is registered
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            # if user is authenticated
            if user:
                #   get existing token or create a new one
                # #Formul : token, created = Token.objects.get_or_create(user=instance)
                token, _ = Token.objects.get_or_create(user=user)

                return Response({
                    'user': UserRegistrationSerializer(user).data,
                    'token': token.key
                }, status=status.HTTP_200_OK)
            
            #if authentication fails, return unauthorised error
            #formu: return Response({'error': <msg>}, status=401)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):          
        user = request.user
        # Formula: serializer = SerializerClass(instance)
        # Turn the user object into JSON data
        serializer = UserRegistrationSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)