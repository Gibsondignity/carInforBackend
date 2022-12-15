import json
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_POST
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from .serializers import UserSerializer, CarInfoSerializer
from .models import CarInfo

# pytesseract imports
from PIL import Image
from pytesseract import pytesseract


def get_csrf(request):
    response = JsonResponse({"Info": "Success - Set CSRF cookie"})
    response["X-CSRFToken"] = get_token(request)
    return response


@require_POST
def loginView(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    if username is None or password is None:
        return JsonResponse({"info": "Username and Password is needed"})

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({"info": "User does not exist"}, status=400)

    login(request, user)
    return JsonResponse({"info": "User logged in successfully"})


class userInfo(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, format=None):
        user = UserSerializer(request.user).data
        print(user)
        return Response(user)
        
        
# @permission_classes((permissions.AllowAny,))
class CarDetails(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, format=None):
        
        data = request.data
        print(data.get("car_number"))
        
        if data.get("car_number") is not None:
            data = get_object_or_404(CarInfo, car_number=request.data.get("car_number"))
            serializer = CarInfoSerializer(data)
            # print(serializer.data)
            return Response(serializer.data)
        
        return Response({"info": "Enter a valid car number"}, status=400)
        
        
# C:\Program Files\Tesseract-OCR\tesseract.exe
class OCR(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, format=None):
        
        data = request.data
        print(data.get("image"))
        
        if data.get("image") is not None:
            # Define path to tessaract.exe
            path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            # Define path to image
            path_to_image = data.get("image")
            # Point tessaract_cmd to tessaract.exe
            pytesseract.tesseract_cmd = path_to_tesseract
            # Open image with PIL
            img = Image.open(path_to_image)
            # Extract text from image
            text = pytesseract.image_to_string(img)
            print(text)
            if text is not None:
                data = get_object_or_404(CarInfo, car_number=request.data.get("car_number"))
                serializer = CarInfoSerializer(data)
                return Response(serializer.data)
            
            return Response({"info": "No text found"}, status=400)
        
        return Response({"info": "Enter a valid image path"}, status=400)
