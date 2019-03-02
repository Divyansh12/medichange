from django.urls import path,include
from .api import *
from knox import views as knox_views

urlpatterns = [
    path('api/auth',include('knox.urls')),
    path('api/auth/register',RegisterAPI.as_view()),
    path('api/auth/login',LoginAPI.as_view()),
    path('api/auth/user',UserAPI.as_view()),
    path('api/auth/logout',knox_views.LogoutView.as_view(),name='logout'),
    path('api/auth/pharmacist/register',PharmacistRegisterAPI.as_view()),
    path('api/auth/pharmacist/login',PharmacistLoginAPI.as_view()),
    path('api/auth/pharmacist',PharmacistAPI.as_view()),
    path('api/auth/organisation/register',OrganisationRegisterAPI.as_view()),
    path('api/auth/organisation/login',OrganisationLoginAPI.as_view()),
    path('api/auth/organisation',OrganisationAPI.as_view()),
]