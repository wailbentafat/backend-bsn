from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RegisterSerializer
from rest_framework.permissions import AllowAny
class RegisterView(APIView):
    permission_classes = [AllowAny]
  
    def post(self, request):
        print("Request data:", request.data)
        serializer = RegisterSerializer(data=request.data)
        print("Serializer:", serializer)
        if serializer.is_valid():
            serializer.save()
            print("User registered successfully.")
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        print("Serializer errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
