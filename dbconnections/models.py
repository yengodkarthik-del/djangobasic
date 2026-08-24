from django.db import models

# Create your models here.
class login(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def _str_(self):
        return self.username



class courses(models.Model):
    course_name=models.CharField(max_length=100)
    price=models.IntegerField()

    def _str_(self):
        return self.course_name



class nav_bar(models.Model):
    name=models.CharField(max_length=100)
    link=models.URLField()

    def _str_(self):
        return self.name


class movie_card(models.Model):
    movie_name=models.CharField(max_length=100)
    genre=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to='images/')
    rating=models.FloatField()

    def _str_(self):
        return self.movie_name




class ticket_booking(models.Model):
    name=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    number_of_tickets=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    phone_no=models.CharField(max_length=10)

    def _str_(self):
        return self.name


class id_card(models.Model):
    name=models.CharField(max_length=100)
    id_number=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=10)
    address=models.TextField()
    image=models.ImageField(upload_to='images/')
    organization=models.CharField(max_length=100)

    def _str_(self):
        return self.name


class laptop(models.Model):
    brand=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    price=models.IntegerField()
    specifications=models.TextField()
    image=models.ImageField(upload_to='images/')

    def _str_(self):
        return self.brand



class attendance(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()
    status=models.CharField(max_length=10)

    def _str_(self):
        return self.name



class results(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    internal_marks=models.IntegerField()
    external_marks=models.IntegerField()
    total_marks=models.IntegerField()
    percentage=models.FloatField()

    def _str_(self):
        return self.name



class rapido_booking(models.Model):
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=10)
    pickup_location=models.CharField(max_length=100)
    drop_location=models.CharField(max_length=100)
    vehicle_type=models.CharField(max_length=50)

    def _str_(self):
        return self.name