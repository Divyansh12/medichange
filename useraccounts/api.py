from rest_framework import generics,permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *
from rest_framework.decorators import action, parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser,FormParser

#Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class= UserRegisterSerializer
    def post(self,request,*args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)
        })

# Login Api

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request,*args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        
        return Response({
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)
        })


#Get User Api

class UserAPI(generics.RetrieveAPIView):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

#Register API
class PharmacistRegisterAPI(generics.GenericAPIView):
    serializer_class= PharmacistRegisterSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def post(self,request,*args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": PharmacistSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)
        })


class PharmacistLoginAPI(generics.GenericAPIView):
    serializer_class = PharmacistLoginSerializer
    # parser_classes = (MultiPartParser, FormParser,)

    
    def post(self,request,*args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        print(user)

        data={"data":Pharamcy.objects.all().filter(email=user) }
        if data['data'] :
            return Response({
            # "user": UserSerializer(user,context=self.get_serializer_context()).data,
                "pharmacist": Pharamcy.objects.values('id','username','email','phoneNumber','aadhaarNo','address','latitude','longitude','licenseOfPharmacist').filter(email=user),
                "token": AuthToken.objects.create(user)
            })
           
        else:
            return Response({
                "details":"Invaid Credentials"
            })

           




class PharmacistAPI(generics.RetrieveAPIView):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    
    serializer_class = PharmacistSerializer
    parser_classes = (MultiPartParser, FormParser,)


    def get(self,request,*args, **kwargs):
        print(self.request.user)

        data={"data":Pharamcy.objects.all().filter(email=self.request.user) }
        print(data)
        if data['data'] :
            return Response({
            "pharmacist": Pharamcy.objects.values('id','username','email','phoneNumber','aadhaarNo','address','latitude','longitude','licenseOfPharmacist').filter(email=self.request.user),
        }) 
        

        else:
            return Response({
                "details":"Invaid"
            })

          

class OrganisationRegisterAPI(generics.GenericAPIView):
    serializer_class= OrganisationRegisterSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def post(self,request,*args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": OrganisationSerializer(user,context=self.get_serializer_context()).data,
            "token":AuthToken.objects.create(user)
        })


class OrganisationLoginAPI(generics.GenericAPIView):
    serializer_class = OrganisationLoginSerializer
    # parser_classes = (MultiPartParser, FormParser,)

    
    def post(self,request,*args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        print(user)
        data={"data":Organisation.objects.all().filter(email=self.request.user) }
        print(data)
        if data['data'] :

            return Response({
            # "user": UserSerializer(user,context=self.get_serializer_context()).data,
                "Organisation": Organisation.objects.values('id','username','email','phoneNumber','aadhaarNo','address','latitude','longitude','licenseOfOrganisation').filter(email=user),
                "token": AuthToken.objects.create(user)
            })
            
        else:

            return Response({
                "details":"Invaid Credentials"
            })

            



class OrganisationAPI(generics.RetrieveAPIView):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    
    serializer_class = OrganisationSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def get(self,request,*args, **kwargs):
        print(self.request.user)
        data={"data":Organisation.objects.all().filter(email=self.request.user) }
        if data['data'] :
            return Response({
                "organisation": Organisation.objects.values('id','username','email','phoneNumber','aadhaarNo','address','latitude','longitude','licenseOfOrganisation').filter(email=self.request.user),
            }) 
           
        else:   
            return Response({
                "details":"Invaid"
            })

           