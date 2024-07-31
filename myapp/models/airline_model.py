from django.db import models


class Airline(models.Model):
    name = models.CharField(max_length=50, null=False)

    @classmethod
    def create(cls, name):
        try:
            Airline(name=name).save()
            return True

        except:
            return False

