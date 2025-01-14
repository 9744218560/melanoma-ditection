from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    usertype=models.CharField(max_length=100,null=True,blank=True)

class UserTable (models.Model):
    loginid = models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=100,null=True,blank=True)
    blood_group = models.CharField(max_length=100,null=True,blank=True) 
    skintype = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    phone_no = models.CharField(max_length=100,null=True,blank=True)
    district = models.CharField(max_length=100,null=True,blank=True)
    previous_history = models.CharField(max_length=100,null=True,blank=True)

class Complaints (models.Model):
     USER = models.ForeignKey(UserTable, on_delete=models.CASCADE, null=True, blank=True)
     complaints = models.CharField(max_length=100,null=True,blank=True)
     date = models.DateField(null=True,blank=True)
     Reply = models.CharField(max_length=100,null=True,blank=True)

class Feedback (models.Model):
    USER = models.ForeignKey(UserTable, on_delete=models.CASCADE, null=True, blank=True)
    feedback = models.CharField(max_length=100,null=True,blank=True)
    Rating = models.CharField(max_length=100,null=True,blank=True)


class Detectiondata (models.Model):
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    descripton = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateField(null=True,blank=True)
