from django.db import models

class User(models.Model):  
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "User"

    name = models.CharField(max_length = 100)
    age = models.PositiveIntegerField(null=True)
    sex = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=False)