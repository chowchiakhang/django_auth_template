from rest_framework.views import APIView
from rest_framework.response import Response

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
