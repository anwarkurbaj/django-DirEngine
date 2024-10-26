from django.db import models
'''
django model fields :
1-html widjet 
2-valdition
3-db size
'''
# Create your models here.# taple in data base =class
# coulmn in data base = filed 
class home(models.Model):# inhertans to acsses filed
    title =models.CharField(max_length=100)# like coulmn in data base 
    
