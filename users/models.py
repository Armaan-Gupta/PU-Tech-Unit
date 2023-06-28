from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):          # this model creates a one-to-one relationship with the existing user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)    # CASCADE: delte this model if the user is deleted
    image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')

    def __str__(self):               # makes the profile more descreiptive
        return f'{self.user.username} Profile'
