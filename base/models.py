from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True, max_length=254)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username']

class Application(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256)
    middle_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    birth_date = models.DateField()
    student_photo = models.ImageField(upload_to='student_photos/')
    father_name = models.CharField(max_length=256)
    mother_name = models.CharField(max_length=256)
    local_address = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    district = models.CharField(max_length=256)
    taluka = models.CharField(max_length=256)
    pincode = models.CharField(max_length=10)
    permanent_address = models.CharField(max_length=256)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    nationality = models.CharField(max_length=256)
    mother_tongue = models.CharField(max_length=256)
    marital_status = models.CharField(max_length=256)
    occupational_status = models.CharField(max_length=256)
    blood_group = models.CharField(max_length=5)
    handicap = models.BooleanField(default=False)
    is_organ_donor = models.BooleanField(default=False)
    conveyance_use = models.CharField(max_length=256)
    religion = models.CharField(max_length=256)
    caste = models.CharField(max_length=256)
    sub_caste = models.CharField(max_length=256)
    caste_validity_no = models.CharField(max_length=256)
    is_minority = models.BooleanField(default=False)
    minority_detail = models.CharField(max_length=256)
    computer_course = models.CharField(max_length=256)
    specialization = models.CharField(max_length=256)

