from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate


#User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','username','email','phoneNumber','aadhaarNo','totalCredits','address')

#Register Serializer

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id','username','email','phoneNumber','aadhaarNo','address','password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        user = UserModel.objects.create_user(username=validated_data['username'],email=validated_data['email'],password=validated_data['password'],phoneNumber=validated_data['phoneNumber'],address=validated_data['address'],aadhaarNo=validated_data['aadhaarNo'])

        return user

#Login Users
class LoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credentials Not Found")

class PharmacistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharamcy
        fields = ('id','username','email','phoneNumber','aadhaarNo','totalCredits','address','latitude','longitude','licenseOfPharmacist')
        
        read_only_fields = ('id','username','email','phoneNumber','aadhaarNo','totalCredits','address','latitude','longitude','licenseOfPharmacist')
        # fields = '__all__'

class PharmacistRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharamcy
        fields = ('id','username','email','phoneNumber','aadhaarNo','address','latitude','longitude','licenseOfPharmacist','password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        user = Pharamcy.objects.create_user(username=validated_data['username'],email=validated_data['email'],password=validated_data['password'],phoneNumber=validated_data['phoneNumber'],address=validated_data['address'],aadhaarNo=validated_data['aadhaarNo'],latitude=validated_data['latitude'],longitude=validated_data['longitude'],licenseOfPharmacist=validated_data['licenseOfPharmacist'])

        return user


class PharmacistLoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credentials Not Found")

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ('id','username','email','phoneNumber','aadhaarNo','totalCredits','address','latitude','longitude','licenseOfOrganisation')
        
        # read_only_fields = ('id','username','email','phoneNumber','aadhaarNo','totalCredits','address','latitude','longitude','licenseOfOrganisation')
        # fields = '__all__'

class OrganisationRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ('id','username','email','phoneNumber','aadhaarNo','address','latitude','longitude','licenseOfOrganisation','password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        user = Organisation.objects.create_user(username=validated_data['username'],email=validated_data['email'],password=validated_data['password'],phoneNumber=validated_data['phoneNumber'],address=validated_data['address'],aadhaarNo=validated_data['aadhaarNo'],latitude=validated_data['latitude'],longitude=validated_data['longitude'],licenseOfOrganisation=validated_data['licenseOfOrganisation'])

        return user


class OrganisationLoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credentials Not Found")

