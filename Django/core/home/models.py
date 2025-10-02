from django.db import models

# define the schema of the database
# Create your models here.
class Student(models.Model):
    # id = models.AutoField() #automatic store in the database as a default primary key
    name = models.CharField(max_length=100, null=False )
    age = models.IntegerField(default=5)
    Student_class = models.IntegerField()
    email = models.EmailField(null=False)
    address = models.TextField(null=False)


class car(models.Model):


    car_name = models.CharField(max_length=500)
    M_Speed = models.IntegerField(default=50)
    L_Speed = models.IntegerField(default=0)

# do this in shell for create many object at once
# car.objects.bulk_create([
#     car(car_name="nexon", M_Speed=91),
#     car(car_name="bmw", M_Speed=191)
# ])

# Create
# Create a new Car object and save it to the database
# car = Car(car_name="nexon", M_Speed=91)
# car.save()

# Read
# # Get all Car objects
# cars = Car.objects.all()

# # Get a single Car by id
# car = Car.objects.get(id=1)

# # Filter Cars by a field
# fast_cars = Car.objects.filter(M_Speed__gt=100)

# Update

# # Update an existing Car
# car = Car.objects.get(id=1)
# car.car_name = "updated name"
# car.save()

# Delete
# Delete a Car object
# car = Car.objects.get(id=1)
# car.delete()
