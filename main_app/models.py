
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from typing import TYPE_CHECKING
from django.db import models
from django.urls import reverse

# Create your models here.


class Member(models.Model):
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name




class Pet(models.Model):
  DOG = 'DOG'
  CAT = 'CAT'
  OTHER = 'PET'
  PET_TYPE = [
    (DOG, 'Dog'),
    (CAT, 'Cat'),
    (OTHER, 'Other')
  ]
  type = models.CharField(max_length=3, choices=PET_TYPE, default=DOG)
  name = models.CharField(max_length=100, blank=False)
  breed = models.CharField(max_length=100, blank=False)
  city = models.CharField(max_length=100, blank=False)
  state = models.CharField(max_length=100, blank=False)
  breed = models.CharField(max_length=100, blank=False)
  MALE = 'Male'
  FEMALE = 'Female'
  PET_SEX = [
    (MALE, 'Male'),
    (FEMALE, 'Female')
  ]
  sex = models.CharField(max_length=6, choices=PET_SEX, default=MALE)
  comments = models.TextField(blank=True)
  LOST = 'LOST'
  FOUND = 'FOUND'
  STATUS_OPTIONS = [
    (LOST, 'Lost'),
    (FOUND, 'Found')
  ]
  status = models.CharField(max_length=5, choices=STATUS_OPTIONS, default=LOST)
  member = models.ForeignKey(Member, null=True, on_delete= models.SET_NULL)
  
  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("detail", kwargs={'pet_id':self.id})
  
class Photo(models.Model):
  pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
  url = models.CharField(max_length=200, default='https://sugarplumnannies.com/wp-content/uploads/2015/11/dog-placeholder.jpg')
  def __str__(self):
     return f"Lost pet photo for pet_id: {self.pet_id} @{self.url}"
  