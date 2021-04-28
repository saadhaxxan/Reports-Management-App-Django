from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to='customers',default="default.jpg")

    def __str__(self):
        return str(self.name)

