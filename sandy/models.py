from django.db import models

# Create your models here.
  
class Home(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    heading = models.CharField(max_length=50, default='')
    description = models.TextField(blank=False, default='')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    
class Service(models.Model):
    networking = models.TextField(blank=False)
    sysadmin = models.TextField(blank=False)
    server_infrastructure = models.TextField(blank=False)
    updated = models.DateTimeField(auto_now=True)

class Portfolio(models.Model):
    image_1 = models.ImageField(upload_to='portfolio/')
    image_2 = models.ImageField(upload_to='portfolio/', default='')
    image_3 = models.ImageField(upload_to='portfolio/', default='')
    project_1 = models.CharField(max_length=50, default='')
    project_2 = models.CharField(max_length=50, default='')
    project_3 = models.CharField(max_length=50, default='')
    description_1 = models.TextField(blank=False, default='')
    description_2 = models.TextField(blank=False, default='')
    description_3 = models.TextField(blank=False, default='')
    updated = models.DateTimeField(auto_now=True)
    
class Education(models.Model):
    institution_1 = models.CharField(max_length=50)
    major_1 = models.TextField(max_length=60)
    start_1 = models.CharField(max_length=10, default='')
    end_1 = models.CharField(max_length=10, default='')
    institution_2 = models.CharField(max_length=50, default='')
    major_2 = models.TextField(max_length=60, default='')
    start_2 = models.CharField(max_length=10, default='')
    end_2 = models.CharField(max_length=10, default='')
    skills_desc = models.TextField(blank=False, default='')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.institution_1