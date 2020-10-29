from django.db import models
from django.contrib.auth.models import User, AbstractUser
 

# Create your models here...

class DateAbstractModel(models.Model):
    create_at= models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class DateStartEndAbstractModel(models.Model):
    start_date= models.DateTimeField(auto_now=True)
    end_date= models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True        
 
class Role(DateAbstractModel):
    name= models.CharField(blank=True, null=True, max_length=50)
     
    can_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.name
class Countries(models.Model):
    name= models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name                

class RussianRegion(models.Model):
    country= models.ForeignKey(Countries, on_delete=models.CASCADE, related_name='russionregion')
    number = models.IntegerField()
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name   



        
class Location(models.Model):
    city=models.CharField(max_length=255, null=True)
    lat=models.CharField(max_length=20, null=True)
    lon=models.CharField(max_length=20, null=True)
    country=models.ForeignKey(Countries, on_delete=models.CASCADE, related_name='location')
    russionregion= models.ForeignKey(RussianRegion, on_delete=models.CASCADE, related_name='region', null=True)
    state=models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.city        

class userProfile(models.Model):    
    user=models.OneToOneField('auth.User',on_delete=models.CASCADE,related_name="profile")
    description=models.TextField(blank=True,null=True)
    location=models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)    
    birthday=models.DateTimeField(null=True)
    role=models.ForeignKey(Role, related_name='roles', on_delete=models.CASCADE, default=2)
    is_student=models.BooleanField(default=False)
    is_employee=models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='profiles', null=True)
    middle_name=models.CharField(max_length=50,blank=True)
    status= models.CharField(max_length=30,blank=True)
    new_email = models.EmailField(max_length=254, null=True)
    bun_time=models.DateTimeField(null=True)
    bun_reason= models.CharField(max_length=30,blank=True)
    phone_number = models.CharField(max_length=30, null=True, unique=True)     

    def __str__(self):
        return self.user.username




 
class Student(models.Model):
    user=models.OneToOneField('auth.User',on_delete=models.CASCADE,related_name="student")
    prof_camp_participation = models.CharField(max_length=255, blank=True, null=True)
    achievements = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    relation = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.user.username

class Employee(models.Model):
    user=models.OneToOneField('auth.User',on_delete=models.CASCADE,related_name="employee")
    passport_number= models.CharField(max_length=255, blank=True, null=True, unique=True)
    registration = models.CharField(max_length=255, blank=True, null=True)
    INN = models.CharField(max_length=255, blank=True, null=True,  unique=True)
    SNILS = models.CharField(max_length=255, blank=True, null=True,  unique=True)   
    def __str__(self):
        return self.user.username     

class Position(models.Model):
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='position')
    name = models.CharField(max_length=100, blank=True, null=True)
    note =  models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name



class Organization(models.Model):
    name=models.CharField(max_length=255, null=True)     
    location=models.ForeignKey(Location, on_delete=models.CASCADE, related_name='organization')     
    note=models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.name        

class Externalactivity(DateStartEndAbstractModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, related_name='externalactivity')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=False)
    other_organization = models.CharField(max_length=255, null=True)
    activity= models.CharField(max_length=255, null=True)    
    note= models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.activity

class Contract(DateStartEndAbstractModel):
    text = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.text

class Place(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='place')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, null=True)
    contacts= models.CharField(max_length=255, null=True)  
    note = models.CharField(max_length=255, null=True)  
    def __str__(self):
        return self.organization

class Schoolyear(DateStartEndAbstractModel):
    year= models.CharField(max_length=10, null=True)
    note= models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.year
class Language(models.Model):
    name= models.CharField(max_length=50, null=True) 
    def __str__(self):
        return self.name       

class Grade(models.Model):
     name=models.CharField(max_length=50, null=True) 
     language=models.ForeignKey(Language, on_delete=models.CASCADE)
     match_grade=models.CharField(max_length=255, null=True) 
     def __str__(self):
         return self.name


class Study(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    organization=models.ForeignKey(Organization, on_delete=models.CASCADE)
    grade=models.ForeignKey(Grade, on_delete=models.CASCADE)
    school_year=models.ForeignKey(Schoolyear, on_delete=models.CASCADE)
    note=models.CharField(max_length=255, null=True)

class Speciality(models.Model):
    name=models.CharField(max_length=255, null=True)
    note=models.CharField(max_length=255, null=True) 
    def __str__(self):
         return self.name
         
class Group(models.Model):    
    name = models.CharField(max_length=255, null=True) 
    speciality =models.ForeignKey(Speciality, on_delete=models.CASCADE)
    school_year = models.ForeignKey(Schoolyear, on_delete=models.CASCADE)
    note=models.CharField(max_length=255, null=True)   
    def __str__(self):
         return self.name             

class Olympiad(models.Model):
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    school_year = models.ForeignKey(Schoolyear, on_delete=models.CASCADE)
    note = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.name

class Olympiadplace(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    olympiad= models.ForeignKey(Olympiad, on_delete=models.CASCADE)
    agreement= models.CharField(max_length=100, null=True)
    check_themself= models.IntegerField()
    trust= models.CharField(max_length=100, null=True)
    reception_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.olympiad

class Round(models.Model):
    olympiad=models.ForeignKey(Olympiad, on_delete=models.CASCADE)
    number= models.IntegerField()
    note = models.CharField(max_length=255, null=True)   
    def __str__(self):
        return self.number 

class Olympiadplaceround(models.Model):
    olympiad_place= models.ForeignKey(Olympiadplace, on_delete=models.CASCADE)
    olympiad= models.ForeignKey(Olympiad, on_delete=models.CASCADE)
    round_number=models.ForeignKey(Round, on_delete=models.CASCADE)
    status =models.CharField(max_length=255, null=True)
    note=models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.round_number
class Result(models.Model):
    name= models.CharField(max_length=255, null=True)  
    def __str__(self):
       return self.name    

 


class Olympiadwork(models.Model):
    olympiad= models.ForeignKey(Olympiad, on_delete=models.CASCADE)
    round_number=models.ForeignKey(Round, on_delete=models.CASCADE)
    student= models.ForeignKey(Student, on_delete=models.CASCADE)
    language= models.ForeignKey(Language, on_delete=models.CASCADE)
    examiner= models.ForeignKey(Employee, on_delete=models.CASCADE)
    parallel=models.CharField(max_length=255, null=True)
    file_path=models.FileField(upload_to='olypiadworks')
    status=models.CharField(max_length=255, null=True)
    points= models.IntegerField()
    result=models.ForeignKey(Result, on_delete=models.CASCADE)
    note=models.CharField(max_length=255, null=True)
    def __str__(self):
       return self.result 

class Olympiadjob(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='olympiadjob')
    olympiad=models.ForeignKey(Olympiad, on_delete=models.CASCADE)
    position=models.ForeignKey(Position, on_delete=models.CASCADE)
    note=models.CharField(max_length=255, null=True)  
    def __str__(self):
        return self.olympiad

class Inspectionact(models.Model):
    olypiad_work = models.ForeignKey(Olympiadwork, on_delete=models.CASCADE)
    juror=models.IntegerField()
    parallel_officer=models.IntegerField()
    status=models.CharField(max_length=50, null=True)
    disqualification = models.IntegerField()
    disqualification_reason=models.CharField(max_length=50, null=True)
    note= models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.status


class Task(models.Model):
    inspection_act=models.ForeignKey(Inspectionact, on_delete=models.CASCADE)
    number=models.IntegerField()
    points=models.IntegerField()
    note=models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.number

class Groupcompetitor(models.Model):
    student =models.ForeignKey(Student, on_delete=models.CASCADE)
    group =models.ForeignKey(Group, on_delete=models.CASCADE)
    result = models.CharField(max_length=255, null=True)
    status =models.CharField(max_length=50, null=True)
    note =models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.group

class Camp(DateStartEndAbstractModel):
    tour_name=models.CharField(max_length=255, null=True)
    tour_name_suffics=models.CharField(max_length=50, null=True)
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    note= models.CharField(max_length=255, null=True)       
    def __str__(self):
        return self.tour_name

class CampGroup(models.Model):
    camp=models.ForeignKey(Camp, on_delete=models.CASCADE)
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
    def __str__(self):
        return self.camp

class Campjob(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE,related_name='campjobs')
    camp=models.ForeignKey(Camp, on_delete=models.CASCADE)
    position=models.ForeignKey(Position, on_delete=models.CASCADE)
    note=models.CharField(max_length=255, null=True)       
    def __str__(self):
        return self.position 

class Groupjob(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='groupjobs')
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
    position=models.ForeignKey(Position, on_delete=models.CASCADE)
    note=models.CharField(max_length=255, null=True)   
    def __str__(self):
        return self.employee

class Olympiadcompetitor(models.Model):
    user=models.ForeignKey(userProfile, on_delete=models.CASCADE)
    olympiad= models.ForeignKey(Olympiad, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.user.username



