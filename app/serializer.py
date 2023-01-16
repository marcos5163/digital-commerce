from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User



class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 100, min_length = 7)

    def validate(self, attrs):
        attrs =  super().validate(attrs)

        if User.objects.filter(username = attrs['email']).exists():
            raise ValidationError({"email":"This email already exists"})

        return attrs    

    def create(self, validated_data):

        return User.objects.create(username = validated_data['email'], password = validated_data['password'])  


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 100, min_length = 7)

    def validate(self, attrs):
        attrs =  super().validate(attrs)

        if not User.objects.filter(username = attrs['email'], password = attrs['password']).exists():
            raise ValidationError({"non_field_error":"User doesn't exists"})
        
        if User.objects.filter(username = attrs['email']).exists():
            raise ValidationError({"non_field_error":"Invalid creds"})

        return attrs    
         


            
    



        
     