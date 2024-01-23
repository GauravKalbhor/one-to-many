from django.db import models

# Create your models here.
class Departments(models.Model):
    Department_name = models.CharField(max_length=100)
    Deparment_descrip = models.CharField(max_length= 200)

    def __str__(self):
        return self.Department_name

class Students(models.Model):
    Name = models.CharField(max_length = 100)    
    Email = models.EmailField(max_length = 100)    
    Contact = models.CharField(max_length = 100)    
    Department = models.ForeignKey(Departments,on_delete = models.PROTECT, null=True)    

    def __str__(self):
        return self.Name
    