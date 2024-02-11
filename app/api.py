from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RegisterSerializer, UserSerializer,LoginSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
#Register API

class LoginApi(APIView):
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.validated_data.get("username")
                password = serializer.validated_data.get("password")
                email = serializer.validated_data.get("email")
                
                user = authenticate(request, username=username, password=password)
                if not user:
                    user = authenticate(request, email=email, password=password)

                if user is not None:
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        "refresh": str(refresh),
                        "access": str(refresh.access_token)
                    })
                else:
                    return Response({
                        "status": 400,
                        "message": "Login failed. Invalid credentials.",
                    })
            else:
                return Response({
                    "status": 400,
                    "message": "Login failed.",
                    "errors": serializer.errors
                })
        except Exception as e:
            print(e)
            return Response({
                "status": 500,
                "message": "An error occurred while processing your request."
            })
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.validated_data.get("username")
                password = serializer.validated_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        "refresh": str(refresh),
                        "access": str(refresh.access_token)
                    })
                else:
                    return Response({
                        "status": 400,
                        "message": "Login failed. Invalid credentials.",
                    })
            else:
                return Response({
                    "status": 400,
                    "message": "Login failed.",
                    "errors": serializer.errors
                })
        except Exception as e:
            print(e)
            return Response({
                "status": 500,
                "message": "An error occurred while processing your request."
            })

class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully. Now perform Login to get your token",
        })
class UserListApi(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    