from .models import *
from rest_framework import serializers
from graphene_django.rest_framework.mutation import SerializerMutation



class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medicine
        fields = '__all__'


class MedicineOfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicineOfUser
        fields='__all__'
        

class MedicineLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicineOfUser
        fields=('id','creditForMedicine','quantityOfMedicine','expiryDate','pharmacist')
