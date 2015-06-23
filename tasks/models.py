import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class CurrentTask(models.Model):

    task = models.CharField(max_length=255)
    ONCE = 'One Time'
    WEEKLY = 'Weekly'
    MONTHLY = 'Monthly'
    FREQUENCY_CHOICES = ((ONCE, 'One Time'), (WEEKLY, 'Weekly'), (MONTHLY, 'Monthly'))
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default=ONCE)

    #pub_date = models.DateTimeField('date published')
    date_due = models.DateTimeField('date due')
    #email = models.EmailField(max_length=254)

    def __unicode__(self):
        return self.task

class TaskType(models.Model):
    type = models.ForeignKey(CurrentTask)
    description = models.CharField(max_length=600)
    person_in_charge = models.ForeignKey(User)

    def __unicode__(self):
        return self.description