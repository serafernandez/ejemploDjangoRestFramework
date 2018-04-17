from django.db import models

# Create your models here.

class Todos(models.Model):

    task = models.CharField(max_length = 500)
    done = models.BooleanField(default=False)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)