from django.shortcuts import render
from .serializers import *
from .models import *
from decimal import Decimal
from django_filters import rest_framework as djfilters
import django_filters
from django.db.models import Count,Avg,Sum
from rest_framework.response import Response
from rest_framework import viewsets,permissions,filters,views
from rest_framework.parsers import JSONParser, MultiPartParser,FormParser
from useraccounts.serializers import PharmacistSerializer
from useraccounts.models import UserModel,Pharamcy,Organisation
from django.http import Http404
import io
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import Storage
from django.core.files.base import ContentFile
from django.shortcuts import render
import io
import os
from google.cloud import vision
from google.cloud.vision import types

import datetime
from PIL import Image
import pytesseract


class CommenViewSet(viewsets.ModelViewSet):
	permission_classes  = (permissions.AllowAny,)
	filter_backends = (filters.OrderingFilter,filters.SearchFilter,djfilters.DjangoFilterBackend,)
	filterset_fields = '__all__'
	search_fields = '__all__'
	ordering_fields = '__all__'
	extra_permissions = None
	def get_permissions(self):
		"""
		Instantiates and returns the list of permissions that this view requires.
		"""
		extra = []
		if self.extra_permissions is not None:
			extra = [permission() for permission in self.extra_permissions]
		return [permission() for permission in self.permission_classes]+extra



class MedicineViewSet(CommenViewSet):

   serializer_class = MedicineSerializer
   queryset = Medicine.objects.all()

# class MedicineOfUserFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='iexact')

#     class Meta:
#         model = MedicineOfUser
#         exclude = ['medicinePicture','expiryPicture']
#         filter_overrides = {
#             models.ImageField: {
#                 'filter_class': django_filters,
#                 'extra': lambda f: {
#                     'lookup_expr': 'icontains',
#                 },
#             },
#         }
class MedicineOfUserViewSet(viewsets.ModelViewSet):

    permission_classes=[
        permissions.IsAuthenticated
    ]
    serializer_class = MedicineOfUserSerializer
    def get_queryset(self):
        return self.request.user.medicineOfUser.all()
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    # def destroy(self,request,*args, **kwargs):
    # # delete an object and send a confirmation response

    #     instance = self.get_object()
    #     print(instance.id)
    #     MedicineOfUser.objects.get(id=instance.id).delete()
    #     return Response({
    #         "medicine":MedicineOfUser.objects.all().filter(user=self.request.user),
    #         "details":"Deleted"
    #         })

# def DeleteMedicineOfUserViewSet(views.APIView):

#     def patch(self,request,*args,**kwargs):
#         print(self.request.user)
#         print(self.request)
#         req=request.POST

#         setrequest=False

#         print(req.get("id"))
#         updated = MedicineOfUser.objects.filter(pharmacist=self.request.user.id,isRequested=True,id=req.get("id")).update(isRequested=setrequest,isAccepteByPharmacist=req.get("isAccepteByPharmacist")),
#         return Response({ 
#             "details":MedicineOfUser.objects.values('id','creditForMedicine','medicine__name','quantityOfMedicine','expiryDate','medicinePicture','expiryPicture','pharmacist').filter(pharmacist=self.request.user.id,isRequested=True),
#             })



class MedicineLocationViewSet(views.APIView):
	def get(self,request,*args,**kwargs):
		data={}

		data['medicineLocation']= MedicineOfUser.objects.values('id','medicine__name','medicine__id','creditForMedicine','quantityOfMedicine','expiryDate','pharmacist__username','pharmacist__address','pharmacist__latitude','pharmacist__longitude').filter(isAcceptedByPharmacist=True)

		return Response(data)

class RequestViewSet(views.APIView):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    
    serializer_class = PharmacistSerializer


    def get(self,request,*args, **kwargs):
        print(self.request.user)
        # print(dict(self.request))

        data={"data":Pharamcy.objects.all().filter(email=self.request.user) }
        print(data)
        if data['data'] :
            return Response({
            "request": MedicineOfUser.objects.values('id','creditForMedicine','medicine__name','quantityOfMedicine','expiryDate','medicinePicture','expiryPicture','pharmacist').filter(pharmacist=self.request.user.id,isRequested=True),
        }) 
        

        else:
            return Response({
                "details":"Invaid"
            })
    def patch(self,request,*args,**kwargs):
        print(self.request.user)
        print(self.request)
        req=request.POST

        print(req.get("id"))
        updated = MedicineOfUser.objects.filter(pharmacist=self.request.user.id,isRequested=True,id=req.get("id")).update(isRequested=req.get("isRequested")),
        return Response({ 
            "details":MedicineOfUser.objects.values('id','creditForMedicine','medicine__name','quantityOfMedicine','expiryDate','medicinePicture','expiryPicture','pharmacist').filter(pharmacist=self.request.user.id,isRequested=True),
            })


class AcceptViewSet(views.APIView):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    
    serializer_class = PharmacistSerializer

    def patch(self,request,*args,**kwargs):
        print(self.request.user)
        print(self.request)
        req=request.POST

        setrequest=False

        print(req.get("id"))
        updated = MedicineOfUser.objects.filter(pharmacist=self.request.user.id,isRequested=True,id=req.get("id")).update(isRequested=setrequest,isAcceptedByPharmacist=req.get("isAcceptedByPharmacist")),
        return Response({ 
            "details":MedicineOfUser.objects.values('id','creditForMedicine','medicine__name','quantityOfMedicine','expiryDate','medicinePicture','expiryPicture','pharmacist').filter(pharmacist=self.request.user.id,isRequested=True),
            })

    

# class EventViewSet(CommenViewSet):
#     serializer_class = EventSerializer
#     queryset = Event.objects.all()

# class Calculate(views.APIView):
#     def get(self,request,*args,**kwargs):
#         users = CustomUser.objects.filter(archived=False)
#         eventNumbers = {}
#         # Getting number of events of each event types we have
#         for event in Event.objects.values('eventType').annotate(count = Count('eventType')):
#             eventNumbers[event['eventType']] = event['count']
#         eventTypes = EventType.objects.filter(archived=False)
#         for user in users:
#             participated = {}
#             score = 0
#             # Getting how many events per event Type per participant 
#             for participate in Participated.objects.values('event__eventType').annotate(count = Count('event__eventType')).filter(user=user):
#                 participated[participate['event__eventType']] = participate['count']
#             for eventType in eventTypes:
#                 # If student didn't participate they will give error and that error will be skipped
#                 try:
#                     normalizedAvg = Participated.objects.filter(event__eventType = eventType,user=user).aggregate(score=Avg('score'))
#                     normalizedAvg = normalizedAvg['score']
#                     trident = participated[eventType.id]/eventNumbers[eventType.id]
#                     score = score + trident*float(eventType.phi)*normalizedAvg
#                 except:
#                     score = score
#             # Gender Bias
#             if user.gender == "F":
#                 score = score*1.05
#             user.score = score
#             user.save()
#         return Response({"msg":"It works!!!"}) 

class CalculateCreditTotal(views.APIView):
    def get(self,request,*args,**kwargs):
        Users = UserModel.objects.all()
        
        for participate in MedicineOfUser.objects.values('user__id').annotate(sum=Sum('creditForMedicine')).filter(isAcceptedByPharmacist=True):
            updated = UserModel.objects.filter(id=participate['user__id']).update(totalCredits=participate['sum'])
        return Response({"msg":"It Works"}) 

class Transaction(views.APIView):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    
    serializer_class = PharmacistSerializer


    def get(self,request,*args, **kwargs):
        print(self.request.user)

        data={"data":Pharamcy.objects.all().filter(email=self.request.user) }

        medicines = MedicineOfUser.objects.values('id','creditForMedicine','medicine__name','quantityOfMedicine','expiryDate','medicinePicture','expiryPicture','user','user__totalCredits','pharmacist','pharmacist__totalCredits','isAcceptedByPharmacist').filter(pharmacist=self.request.user.id,isAcceptedByPharmacist=True)

        for meds in medicines:
            if meds['isAcceptedByPharmacist']==True:
                meds['user__totalCredits'] = meds['user__totalCredits'] + meds['creditForMedicine']
                meds['pharmacist__totalCredits'] = meds['pharmacist__totalCredits'] - meds['creditForMedicine']
                updateuser=UserModel.objects.filter(id=meds['user']).update(totalCredits=meds['user__totalCredits'])
                updatePharma=Pharamcy.objects.filter(id=meds['pharmacist']).update(totalCredits=meds['pharmacist__totalCredits'])
                update=MedicineOfUser.objects.filter(id=meds['id']).update(isRequested = False)
                print(update)



        return Response({"detail":"transaction completed"})

class DateWiseCreditUpdateViewSet(views.APIView):
    def get(self,request,*args, **kwargs):

        for medicines in MedicineOfUser.objects.all():
            diff=datetime.datetime.now().date()-medicines.expiryDate
            # datetime.datetime.now().date()-
            
            if(diff.days<=15):
                credit = medicines.creditForMedicine - medicines.creditForMedicine*0.5
                

            elif(diff.days<=30):
                credit = medicines.creditForMedicine - medicines.creditForMedicine*0.35

            elif(diff.days<=60):
                credit = medicines.creditForMedicine - medicines.creditForMedicine*0.20

            elif(diff.days<=90):
                credit = medicines.creditForMedicine - medicines.creditForMedicine*0.10

            updated = MedicineOfUser.objects.filter(id=medicines.id).update(creditForMedicine=Decimal(credit))
            





            print(diff.days)
        return Response({"completed":"True"})

class MedicineInfoViewSet(views.APIView):

    def get(self,request,*args, **kwargs):

        os.system("set GOOGLE_APPLICATION_CREDENTIALS='C:/Users/Azomicrate/Documents/Desktop2/VsCode/Django/apiauthpreview/test.json'")

        req=request.POST
        client = vision.ImageAnnotatorClient()
        file_name = os.path.join(
            os.path.dirname(__file__),
            req.get("img"))

        with io.open(file_name,'rb') as image_file:
            content= image_file.read()

        image = types.Image(content=content)

        words={}

        response = client.document_text_detection(image=image)
        # labels = response.full_text_annotation.blocks
        # print("Labels:")
        for page in response.full_text_annotation.pages:

            # if page.confidence>0.05:
                for block in page.blocks:
                    print('\nBlock confidence: {}\n'.format(block.confidence))

                    for paragraph in block.paragraphs:
                        print('Paragraph confidence: {}'.format(
                            paragraph.confidence))


                        for word in paragraph.words:

                            words["text"] = ''.join([
                                symbol.text for symbol in word.symbols
                            ])
                            # if word_text=="EXP" or word_text=="exp" or 
                            print(words["text"])
        

        return Response(words)

                        
class AddMedicineRequestViewSet(CommenViewSet):

   serializer_class = AddMedicineRequestSerializer
   queryset = RequestedMedicines.objects.all()

    


                
