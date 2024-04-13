from django.db import models

class operation(models.Model):
    
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    duration = models.CharField(max_length=100, null=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    description = models.TextField(max_length=200,null=True)
    start_date = models.DateField(null=True)
    created_on = models.DateTimeField(null=True)
    updated_on = models.DateTimeField(null=True)
    ratings = models.IntegerField(null=True) 
