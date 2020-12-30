from django.db import models

class Contact(models.Model):
    last_name, surname, email = models.TextField()
    phone = models.IntegerField()
    def __str__(self):
        return self.last_name + " " + self.surname + " " + self.email + " " + self.phone

