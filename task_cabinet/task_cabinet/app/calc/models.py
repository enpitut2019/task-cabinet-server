from django.db import models


class Calc(models.Model):
    first_number = models.BigIntegerField()
    second_number = models.BigIntegerField()
    calc = models.TextField()

    class Meta:
        db_table = 'calc'
