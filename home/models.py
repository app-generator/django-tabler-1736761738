# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Task(models.Model):

    #__Task_FIELDS__
    text = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    duration = models.IntegerField(null=True, blank=True)
    progress = models.IntegerField(null=True, blank=True)
    parent = models.CharField(max_length=255, null=True, blank=True)
    sort_order = models.IntegerField(null=True, blank=True)

    #__Task_FIELDS__END

    class Meta:
        verbose_name        = _("Task")
        verbose_name_plural = _("Task")


class Link(models.Model):

    #__Link_FIELDS__
    source = models.CharField(max_length=255, null=True, blank=True)
    target = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    lag = models.IntegerField(null=True, blank=True)

    #__Link_FIELDS__END

    class Meta:
        verbose_name        = _("Link")
        verbose_name_plural = _("Link")



#__MODELS__END
