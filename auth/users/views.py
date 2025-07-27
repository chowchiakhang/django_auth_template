from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime

from .models import User

from .serialiizers import UserSerializer

# Create your views here.
class RegisterView(APIView):
    """
    View to handle user registration.
    """
    def post(self, request):
        # Logic for user registration will go here
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    """
    View to handle user login.
    """
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now(tz=datetime.timezone.utc)
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        response = Response()

        response.set_cookie(
            key='jwt',
            value=token,
            httponly=True,
            samesite='Strict'
        )

        response.data = {
            'message': 'success',
        }

        return response
    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    
class ForgotView(APIView):
    """
    View to handle password reset requests.
    """
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        
        if not user:
            raise AuthenticationFailed('User not found')
        
        # Logic to send reset link or code goes here
        return Response({'message': 'Password reset link sent'})
    
class ResetView(APIView):
    """
    View to handle password reset.
    """
    def post(self, request):
        token = request.data.get('token')
        new_password = request.data.get('password')
        
        # Logic to verify token and reset password goes here
        # For example, find user by token and set new password
        
        return Response({'message': 'Password has been reset'})