from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import     UserProfileListCreateView,     userProfileDetailView,    UserListCreateView,    StudentDetailView,     EmployeeDetailView,    PositionDetailView, PositionListCreateView, SpecialityListCreateView, SpecialityDetailView, CampjobListCreateView, CampjobDetailView, GroupjobListCreateView, GroupjobDetailView, OlympiadjobListCreateView, OlympiadjobDetailView, GroupDetailView, GroupListCreateView,ExternalactivityListCreateView, ExternalactivityDetailView, LocationListCreateView, LocationDetailView

urlpatterns = [
    #gets all user profiles and create a new profile
    path("all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
   # retrieves profile details of the currently logged in user
    path("profile/<int:pk>",userProfileDetailView.as_view(),name="profile"),
    path("student/<int:pk>",StudentDetailView.as_view(),name="student"),
    path("employee/<int:pk>",EmployeeDetailView.as_view(),name="employee"),
    path("positions/",PositionListCreateView.as_view(),name="positions"),
    path("position/<int:pk>",PositionDetailView.as_view(),name="position-detail"),    
    path("specialties/", SpecialityListCreateView.as_view(), name="speciality-list"),
    path("speciality/<int:pk>", SpecialityDetailView.as_view(), name="speciality"),
    path("campjobs/", CampjobListCreateView.as_view(), name="campjob-list"),
    path("campjob/<int:pk>", CampjobDetailView.as_view(), name="campjob-detail"),
    path("groupjobs/", GroupjobListCreateView.as_view(), name="groupjob-list"),
    path("groubjob/<int:pk>", GroupjobDetailView.as_view(), name="groupjob-detail"),
    path("olympiadjobs/", OlympiadjobListCreateView.as_view(), name="olympiadjob-list"),
    path("olympiadjob/<int:pk>", OlympiadjobDetailView.as_view(), name="olympiadjob-detail"),
    path("groups/", GroupListCreateView.as_view(), name="group-list"),
    path("group/<int:pk>", GroupDetailView.as_view(), name="group-detail"),
    path("externalactivities/", ExternalactivityListCreateView.as_view(), name="externalactivity_list"),
    path("externalactivity/<int:pk>", ExternalactivityDetailView.as_view(), name="externalactivity"),
    path("locations/", LocationListCreateView.as_view(), name="location_list"),
    path("location/<int:pk>", LocationDetailView.as_view(), name="location"),

    path("users",UserListCreateView.as_view(),name="username"),
    
]