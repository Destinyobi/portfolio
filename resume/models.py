from django.db import models

class Message(models.Model):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name
# Create your models here.
