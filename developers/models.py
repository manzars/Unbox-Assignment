from django.db import models
from user.models import User
from common.models import *

# Create your models here.


class Developer(models.Model):
    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name = "developer"

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True)
    designation = models.ForeignKey(
        Designation, on_delete=models.SET_NULL, null=True)
    tech_stack = models.ManyToManyField(TechStack, default=None)
    total_experience = models.FloatField()
    employment_type = models.ForeignKey(
        EmploymentType, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=100)
    annual_ctc = models.FloatField()
    linked_in_profile = models.URLField()
    start_date = models.DateField()
    end_date = models.DateField()
