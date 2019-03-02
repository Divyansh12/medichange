from rest_framework import routers
from .api import *
from django.urls import path,include

router = routers.DefaultRouter()
router.register(r'api/medicinelist',MedicineViewSet,'medicines')
router.register(r'api/medicineofuser', MedicineOfUserViewSet, 'medicineOfUser')


urlpatterns = [
    path('api/medicinelocation', MedicineLocationViewSet.as_view()),
    path('api/request',RequestViewSet.as_view()),
    path('api/accept',AcceptViewSet.as_view()),
]


urlpatterns += router.urls