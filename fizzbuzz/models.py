# Create your models here.
from django.db import models


# Create your models here.
class FizzBuzz(models.Model):
    """
    API Model for FizzBuzz
    """
    fizzbuzz_id = models.AutoField(primary_key=True)
    user_agent = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()