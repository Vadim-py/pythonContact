from django.db import models

class Contact(models.Model):
    last_name = models.TextField()
    surname = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    def __str__(self):
        return self.last_name + " " + self.surname + " " + self.email + " " + self.phone