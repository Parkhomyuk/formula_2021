from rest_framework import serializers
from .models import userProfile, Role, Student, Employee, Position, Speciality, Campjob, Groupjob, Group, Externalactivity, Location
from django.contrib.auth.models import User
 
     
        

class userProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    role=serializers.SlugRelatedField(queryset=Role.objects.all(), slug_field='name')
    class Meta:
        model=userProfile
        fields='__all__'


class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model= Speciality 
        fields='__all__'        

class RoleSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)   
    
    
    class Meta:
        model = Role
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Student   
        fields='__all__'      

class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    campjobs=serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='campjob-detail') 
    groupjobs=serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='groupjob-detail')
    olympiadjob=serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='olympiadjob-detail')
    externalactivity=serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='externalactivity')
    class Meta:
        model = Employee   
        fields=('user','passport_number','registration','INN','SNILS', 'campjobs','groupjobs', 'olympiadjob' ,'externalactivity')  

class PositionSerializer(serializers.ModelSerializer):
     
    class Meta:
        model= Position 
        fields= '__all__'           

class UserSerializer(serializers.ModelSerializer):
    # student =serializers.SlugRelatedField(queryset=Student.objects.all(), slug_field='id')
    # employee =serializers.SlugRelatedField(queryset=Employee.objects.all(), slug_field='id')
    # profile =serializers.SlugRelatedField(queryset=Student.objects.all(), slug_field='id')
    employee = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='employee')
    student = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='student')
    profile = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='profile')

    class Meta:
        model=User
        fields='__all__'          
class CampjobSerializer(serializers.ModelSerializer):
    employee_name= serializers.ReadOnlyField(source='employee.user.username')
    camp_name=serializers.ReadOnlyField(source='camp.tour_name')
    camp_name_suffics=serializers.ReadOnlyField(source='camp.tour_name_suffics')
    position=serializers.ReadOnlyField(source='position.name')
    class Meta:
        model=Campjob 
        fields=('employee_name','camp_name','camp_name_suffics','position')

class GroupjobSerializer(serializers.ModelSerializer):
    employee_name= serializers.ReadOnlyField(source='employee.user.username')
    group_name=serializers.ReadOnlyField(source='group.name')     
    position=serializers.ReadOnlyField(source='position.name')
    class Meta:
        model=Groupjob
        fields=('employee_name','group_name','position','note')

class OlympiadjobSerializer(serializers.ModelSerializer):
    employee_name= serializers.ReadOnlyField(source='employee.user.username')
    olympiad_name=serializers.ReadOnlyField(source='olympiad.name')     
    position=serializers.ReadOnlyField(source='position.name')
    class Meta:
        model=Groupjob
        fields=('employee_name','olympiad_name','position','note')

class GroupSerializer(serializers.ModelSerializer):
    speciality_name=serializers.ReadOnlyField(source='speciality.name')
    school_year=serializers.ReadOnlyField(source='school_year.name')
    class Meta:
        model=Group 
        fields=('pk','name','note','speciality_name','school_year')     

class ExternalactivitySerializer(serializers.HyperlinkedModelSerializer):
    employee_name= serializers.ReadOnlyField(source='employee.user.username')
    organozation_name=serializers.ReadOnlyField(source='organization.name')
    class Meta:
        model=Externalactivity 
        fields=('employee_name', 'organozation_name','start_date','end_date','activity','other_organization','note')        


class LocationSerializer(serializers.ModelSerializer):
    country=serializers.ReadOnlyField(source='country.name')
    class Meta:
        model=Location     
        fields=('city','lat','lon','state','country','russionregion')   