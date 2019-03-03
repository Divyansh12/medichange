from rest_framework import routers
from .api import *
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'api/medicinelist',MedicineViewSet,'medicines')
router.register(r'api/medicineofuser', MedicineOfUserViewSet, 'medicineOfUser')
router.register(r'api/requestamedicine', AddMedicineRequestViewSet, 'medicineOfUser')


urlpatterns = [
    path('api/medicinelocation', MedicineLocationViewSet.as_view()),
    path('api/request',RequestViewSet.as_view()),
    path('api/accept',AcceptViewSet.as_view()),
    path('api/transaction',Transaction.as_view()),
    path('api/credittotal',CalculateCreditTotal.as_view()),
    path('api/creditupdate',DateWiseCreditUpdateViewSet.as_view()),
    path('api/ocr',MedicineInfoViewSet.as_view()),
]


urlpatterns += router.urls