from rest_framework import viewsets, status
from rest_framework.response import Response
from app.serializer import RegisterSerializer, LoginSerializer

# Create your views here

class AuthViewSet(viewsets.ViewSet):
    def check_permissions(self, request):
        return super().check_permissions(request) 

    def login(self, request):
        serializer = LoginSerializer(data= request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error":serializer.errors})

        return Response(status=status.HTTP_200_OK)    

         
        
    def register(self, request):
        serializer = RegisterSerializer(data= request.data)

        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error":serializer.errors})

        serializer.save()

        return Response(status=status.HTTP_200_OK, data={})    

            



        

           

            







         
   