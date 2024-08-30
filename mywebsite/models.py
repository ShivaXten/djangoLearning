from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    desc=models.TextField()
    date=models.DateField()
    
    #this is done so that you can see in the datebase with their name 
    def __str__(self):
        return self.name
   

    
