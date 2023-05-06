from django.db import models

# Create your models here.

class car(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    model=models.CharField(max_length=200)
    price=models.IntegerField()
    description=models.CharField(max_length=200)
    distance=models.IntegerField()
    image=models.ImageField()

    def __str__(self):
        return self.name

class user(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    image=models.ImageField()

    def __str__(self):
        return self.name
    

class Reservation(models.Model):
    id=models.IntegerField(primary_key=True)
    car = models.ForeignKey(car, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()
    return_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user} reserved {self.car} from {self.pickup_date} to {self.return_date}"