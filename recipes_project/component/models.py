from django.db import models

class recipes(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=150)
    cooking_time=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to='recipes/images/')
    date=models.DateField()

    def __str__(self):
        return self.name