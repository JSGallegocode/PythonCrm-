from django.contrib.auth.models import User
from django.db import models

from teams.models import Team

# Create your models here.
class Lead(models.Model):


    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        (LOW,'Low'),
        (MEDIUM, 'Medium'),
        (HIGH , 'High')
    )

    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'


    CHOICES_STATUS = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (WON ,'Won'),
        (LOST, "Lost")
    )

    team = models.ForeignKey(Team, related_name='clients', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank = True, null = True)
    priority = models.CharField(max_length=10, choices = CHOICES_PRIORITY, default=MEDIUM)
    converted_to_client = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name= 'leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length=10, choices = CHOICES_STATUS, default= NEW)


    def __str__(self):
       return self.name
