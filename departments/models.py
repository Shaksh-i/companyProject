from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Department(models.Model):
    # you can omit explicit id and let Django use the default 'id' field.
    deptname = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.deptname

    def get_absolute_url(self):
        return reverse('department_detail', args=[str(self.pk)])
