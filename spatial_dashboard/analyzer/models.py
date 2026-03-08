from django.db import models

class RoomImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    generated_image = models.ImageField(upload_to='generated/', null=True, blank=True)
    room_type = models.CharField(max_length=50)
    lighting = models.CharField(max_length=50)
    person_present = models.BooleanField(default=False)