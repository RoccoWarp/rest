from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=256, unique=True, error_messages={"unique": "A user with that email address already exists."})
