from django.db import models

# DO THIS IN TERMINAL !!!
# python manage.py makemigrations myapp1
# python manage.py migrate

class Worker(models.Model):
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=35, blank=False)
    salary = models.IntegerField(default=0)

# python manage.py createsuperuser
# dzyamon 123

    # def __str__(self):
    #     return f'{self.second_name} {self.name}'