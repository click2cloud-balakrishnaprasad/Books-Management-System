from asyncio.windows_events import NULL
from django.db import models

class Employee(models.Model):
    full_name=models.TextField(max_length=100,default="")
    employee_code = models.TextField(max_length=100,default="")
    mobilenum = models.IntegerField(default=0)

