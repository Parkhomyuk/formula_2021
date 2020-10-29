from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import userProfile, Student, Employee, Position, Speciality, Campjob,Groupjob, Olympiadjob, Group, Externalactivity, Location
from .permission import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer, UserSerializer, StudentSerializer, EmployeeSerializer, PositionSerializer, SpecialitySerializer, CampjobSerializer, GroupjobSerializer, OlympiadjobSerializer, GroupSerializer, ExternalactivitySerializer, LocationSerializer
from django.contrib.auth.models import User
from rest_framework import generics

from rest_framework import filters
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter 
 
 
# Create your views here.

class UserProfileListCreateView(ListCreateAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]

class StudentDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer   
class EmployeeDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer        

class UserListCreateView(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class PositionListCreateView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class= PositionSerializer 
    name="positions" 
    filter_fields=('name','note')
    search_fields=('^name',)
    ordering_fields =('name',)

class PositionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class= PositionSerializer       
    name='position-detail'      

class SpecialityListCreateView(generics.ListCreateAPIView):
    queryset = Speciality.objects.all()
    serializer_class= SpecialitySerializer
     

class SpecialityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Speciality.objects.all()
    serializer_class= SpecialitySerializer
    name='speciality-detail'        

class CampjobListCreateView(generics.ListCreateAPIView):
    queryset = Campjob.objects.all()
    serializer_class= CampjobSerializer   

class CampjobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campjob.objects.all()
    serializer_class= CampjobSerializer      

class GroupjobListCreateView(generics.ListCreateAPIView):
    queryset= Groupjob.objects.all()
    serializer_class= GroupjobSerializer    

class GroupjobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Groupjob.objects.all()
    serializer_class= GroupjobSerializer    


class OlympiadjobListCreateView(generics.ListCreateAPIView):
    queryset= Olympiadjob.objects.all()
    serializer_class= OlympiadjobSerializer    

class OlympiadjobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Olympiadjob.objects.all()
    serializer_class= OlympiadjobSerializer       

class GroupListCreateView(generics.ListCreateAPIView):
    queryset= Group.objects.all()
    serializer_class= GroupSerializer   
    name='group-list'      
    filter_fields=('name',)
    search_fields=('^name',)
    ordering_fields =('name',)

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Group.objects.all()
    serializer_class= GroupSerializer 
    name='group-detail'   
class ExternalactivityListCreateView(generics.ListCreateAPIView):
    queryset= Externalactivity.objects.all()
    serializer_class= ExternalactivitySerializer   
    name='externalactivity-list'      

class ExternalactivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Externalactivity.objects.all()
    serializer_class= ExternalactivitySerializer 
    name='externalactivity'              

class LocationListCreateView(generics.ListCreateAPIView):
    queryset= Location.objects.all()
    serializer_class= LocationSerializer   
    name='location-list'      
    filter_fields=('city','russionregion','country')
    search_fields=('^city',)
    ordering_fields =('country',)

class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Location.objects.all()
    serializer_class= LocationSerializer   
    name='location'  