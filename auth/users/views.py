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

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token,
        }

        return response