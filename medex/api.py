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
    parser_classes = (MultiPartParser, FormParser,)
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

		data['medicineLocation']= MedicineOfUser.objects.values('id','medicine__name','medicine__id','creditForMedicine','quantityOfMedicine','expiryDate','pharmacist__username','pharmacist__address','pharmacist__latitude','pharmacist__longitude').filter(isAccepteByPharmacist=True)

		return Response(data)

class RequestViewSet(views.APIView):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    
    serializer_class = PharmacistSerializer
    parser_classes = (MultiPartParser, FormParser,)


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
    parser_classes = (MultiPartParser, FormParser,)

    def patch(self,request,*args,**kwargs):
        print(self.request.user)
        print(self.request)
        req=request.POST

        setrequest=False

        print(req.get("id"))
        updated = MedicineOfUser.objects.filter(pharmacist=self.request.user.id,isRequested=True,id=req.get("id")).update(isRequested=setrequest,isAccepteByPharmacist=req.get("isAccepteByPharmacist")),
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
        
        for participate in MedicineOfUser.objects.values('user__id').annotate(sum=Sum('creditForMedicine')).filter(isAccepteByPharmacist=True):
            newTotal,updated = UserModel.objects.update(user_id=participate['user__id'],defaults={'totalCredits': participate['sum']})
        return Response({"msg":"It Works"}) 

class Transaction(views.APIView):
    permission_classes=[
        permissions.IsAuthenticated
    ]
    
    serializer_class = PharmacistSerializer
    parser_classes = (MultiPartParser, FormParser,)


    def get(self,request,*args, **kwargs):
        print(self.request.user)

        data={"data":Pharamcy.objects.all().filter(email=self.request.user) }

        medicines = MedicineOfUser.objects.values('id','creditForMedicine','medicine__name','quantityOfMedicine','expiryDate','medicinePicture','expiryPicture','user','pharmacist','isAccepteByPharmacist').filter(pharmacist=self.request.user.id,isRequested=True)

        for meds in medicines:
            if meds.isAcceptedByPharmacist==True:
                meds.user.totalCredit = meds.user.totalCredit + meds.creditForMedicine
                meds.pharmacist.totalCredit = meds.pharmacist.totalCredit - meds.creditForMedine
                meds.isRequested = False
                meds.user.save()
                meds.pharmacist.save()
                meds.save()
