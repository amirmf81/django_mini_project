import datetime
import hashlib

from django.db.models import ObjectDoesNotExist
from django.db import models
from django.db import IntegrityError


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=50, null=False)
    national_id_number = models.CharField(max_length=50, null=False)
    birth_date = models.DateField(null=False)

    @classmethod
    def create_user(
            cls,
            username,
            password,
            phone_number,
            first_name,
            last_name,
            gender,
            national_id_number,
            birth_date,
    ):
        try:
            user = User(
                username=username,
                password=cls.hashed_password(password=password),
                phone_number=phone_number,
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                national_id_number=national_id_number,
                birth_date=birth_date

            )
            user.save()

        except IntegrityError:
            raise IntegrityError

        except AttributeError:
            raise AttributeError

    @classmethod
    def hashed_password(cls, password):
        password_bytes = password.encode('utf-8')
        hashed_password = hashlib.sha256(password_bytes)
        return hashed_password.hexdigest()

    @classmethod
    def check_admin(cls, username):
        try:
            return User.objects.get(username=username).is_admin
        except ObjectDoesNotExist:
            return False

    @classmethod
    def get_user(cls, user_id):
        return User.objects.get(id=user_id)
