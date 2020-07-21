from django.db import models
from datetime import datetime
class Contact(models.Model):
    listing         = models.CharField(max_length=200)
    listing_id      = models.IntegerField()
    name            = models.CharField(max_length=200)
    email           = models.CharField(max_length=50)
    phone           = models.IntegerField()
    message         = models.TextField(blank=True)
    contact_date    = models.DateTimeField(default=datetime.now, blank=True)
    user_id         = models.IntegerField()

    #esta funcion muestra el nombre en la vista
    def  __str__(self):
        return self.name

