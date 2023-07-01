from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True, max_length=254)
    mobile = models.CharField(max_length=15,unique=True)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['username']

class Courses(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,choices=[('ug','UG'),('pg','PG')])


class Application(models.Model):
    ADMISSION_TYPE_CHOICES = [
        ('provisional', 'Provisional'),
        ('non_provisional', 'Non-Provisional'),
    ]
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    className = models.CharField(max_length=20)
    admission_type = models.CharField(max_length=15, choices=ADMISSION_TYPE_CHOICES)
    first_name = models.CharField(max_length=256,blank=True)
    middle_name = models.CharField(max_length=256,blank=True)
    last_name = models.CharField(max_length=256,blank=True)
    birth_date = models.DateField(null=True,blank=True)
    aadhaar_card_no = models.CharField(max_length=12, null=True,blank=True)
    # student_photo = models.ImageField(upload_to='student_photos/', null=True)
    father_name = models.CharField(max_length=256, null=True,blank=True)
    mother_name = models.CharField(max_length=256, null=True,blank=True)
    local_address = models.CharField(max_length=256, null=True,blank=True)
    state = models.CharField(max_length=256, null=True,blank=True)
    district = models.CharField(max_length=256, null=True,blank=True)
    taluka = models.CharField(max_length=256, null=True,blank=True)
    pincode = models.CharField(max_length=10, null=True,blank=True)
    permanent_address = models.CharField(max_length=256, null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    mobile_number = models.CharField(max_length=15, null=True,blank=True)
    nationality = models.CharField(max_length=256, null=True,blank=True)
    mother_tongue = models.CharField(max_length=256, null=True,blank=True)
    marital_status = models.CharField(max_length=256, null=True,blank=True)
    occupational_status = models.CharField(max_length=256, null=True,blank=True)
    blood_group = models.CharField(max_length=5, null=True,blank=True)
    handicap = models.BooleanField(default=False, null=True,blank=True)
    is_organ_donor = models.BooleanField(default=False, null=True,blank=True)
    conveyance_use = models.CharField(max_length=256, null=True,blank=True)
    religion = models.CharField(max_length=256, null=True,blank=True)
    caste = models.CharField(max_length=256, null=True,blank=True)
    sub_caste = models.CharField(max_length=256, null=True,blank=True)
    caste_validity_no = models.CharField(max_length=256, null=True,blank=True)
    is_minority = models.BooleanField(default=False, null=True,blank=True)
    minority_detail = models.CharField(max_length=256, null=True,blank=True)
    computer_course = models.CharField(max_length=256, null=True,blank=True)
    specialization = models.CharField(max_length=256, null=True,blank=True)
