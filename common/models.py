from django.db import models

# Create your models here.

class Designation(models.Model):

    name = models.CharField(max_length = 50, null=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "designation"


class TechStack(models.Model):

    name = models.CharField(max_length = 50, null=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "tech stack"


class EmploymentType(models.Model):

    name = models.CharField(max_length = 50, null=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "employement type"

    