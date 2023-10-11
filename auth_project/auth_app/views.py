from rest_framework import generics,permissions,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .serializers import CustomUserSerializer

class HomeAPIView(APIView):
    pass

class RegistrationAPIView(APIView):
    def post(self,request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 
   
class LoginAPIView(APIView):
    def post(self,request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email,password=password)
        if user:
            login(request,user)
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh":str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_200_OK
            )
        return Response({"error":"Invalid Credentials"},status=status.HTTP_401_UNAUTHORIZED)
@method_decorator(login_required,name="dispatch")      
class LogoutAPIView(APIView):
    def post(self,request):
        logout(request)
        return Response({"message":"Logged out Successfully"}, status=status.HTTP_200_OK)



      
