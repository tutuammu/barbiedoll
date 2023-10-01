from django.db import models

# Create your models here.
class cutie(models.Model):
    name=models.CharField(max_length=150)
    price=models.IntegerField()
    style=models.TextField()
    img=models.ImageField(upload_to='gallery')
    def __str__(self):
        return self.name