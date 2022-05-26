from django.db import models

class blog(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    text=models.TextField()
    image=models.ImageField(upload_to='blog/images/')
    date=models.DateField()

    def __str__(self):
        return self.name