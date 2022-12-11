from django.db import models

# Create your models here.


class Division(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class District(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    division = models.ForeignKey(Division,default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class District(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     division = models.ForeignKey(Division,default=1, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
class Area(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District,default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name