from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    
    # user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    username = models.CharField(max_length=80,blank=True,null=True)
    email=models.EmailField(unique=True)
    aadhaarNo = models.CharField(max_length=12)
    address=models.CharField(max_length=150)
    zipCode=models.CharField(max_length=6)
    totalCredits=models.DecimalField(max_digits=6,decimal_places=2,default=0)
    phoneNumber=models.CharField(max_length=10)
    REQUIRED_FIELDS=['username','aadhaarNo']
    USERNAME_FIELD='email'

    def __str__(self):
        return self.email


class Pharamcy(UserModel):
    latitude=models.CharField(max_length=10000,blank=True,null=True)
    longitude=models.CharField(max_length=10000,blank=True,null=True)
    licenseOfPharmacist=models.FileField(upload_to='pharmacistlicense/',blank=True,null=True)
    licenseNumber = models.CharField(max_length=15,default=0)
    
    def __str__(self):
        return self.email
    


class Organisation(UserModel):
    latitude=models.CharField(max_length=10000,blank=True,null=True)
    longitude=models.CharField(max_length=10000,blank=True,null=True)
    licenseOfOrganisation=models.FileField(upload_to='organisationlicense/',blank=True,null=True)
    licenseNumber = models.CharField(max_length=15,default=0)

    # isHospital=models.BooleanField()
    
    
    def __str__(self):
        return self.email
    