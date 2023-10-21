# Model Managers

```python

class Car(models.Model):
    CAR_MANUFACTURERS = (
        ('Audi','Audi'),
        ('BMW','BMW'),
        ('Ferrari','Ferrari')
    )

    make = models.CharField(max_length = 20, choices = CAR_MANUFACTURERS)
    model = models.CharField(max_length=20)
    year = models.IntegerField(default=2015)

# to access the model manager
Car.objects

# to create a new car
Car.objects.create(make="BMW",model="X5",year=2017)

# QUERYSETS

# retrieving one instance
User.objects.get(username='admin')

# query for all cars in the database
Car.objects.all()

# query for cars with the make equal to "Audi"
Car.objects.filter(make="Audi")

# query for cars with a year greater than 2016
Car.objects.filter(year__gt=2016) #
```
