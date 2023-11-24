from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField(max_length=100)
    description=models.CharField(max_length=250)

    def __str__(self):
        return self.title
