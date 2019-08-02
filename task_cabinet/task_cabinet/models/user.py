from django.db import models
from django.core.validators import MinLengthValidator


class User(models.Model):
    nickname = models.CharField(max_length=30, validators=[MinLengthValidator(5)], unique=True)
    email = models.EmailField()

    def __str__(self):
        return "{}-{}".format(self.nickname, self.email)
