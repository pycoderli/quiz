from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

def validate_even(value):
    i=0
    while value!=0:
        value=value/10
        i=i+1
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

class level(models.Model):
    levelnumber = models.IntegerField(primary_key = True)
    ans = models.CharField(max_length=45)
    pic = models.FileField()

    def __str__(self):
        return str(self.levelnumber)

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=100)
    phoneno = models.IntegerField(validators=[validate_even])
    current_level =  models.ForeignKey('level', on_delete=models.CASCADE, default=1) 
    levelentry = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

    def increaselevel(self):
        l = level.objects.get(levelnumber=(self.current_level.levelnumber+1))
        self.current_level= l
        self.save() 


