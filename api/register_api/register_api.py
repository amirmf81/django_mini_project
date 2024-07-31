from django.http import JsonResponse
from django.db import IntegrityError
from myapp.models.user_model import User
from api.register_api.validation.phone_number import validate_phone_number_func
from api.register_api.validation.username import validate_username_func
from api.register_api.validation.password import validate_password_func
from django.utils.dateparse import parse_date


def register_api_func(
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
        if validate_phone_number_func(phone_number=phone_number):
            if validate_username_func(username=username) and validate_password_func(password=password):
                User.create_user(
                    username=username,
                    password=password,
                    phone_number=phone_number,
                    first_name=first_name,
                    last_name=last_name,
                    gender=gender,
                    national_id_number=national_id_number,
                    birth_date=parse_date(birth_date)
                )
                return JsonResponse({
                    "ok": True,
                    "message": "user created",
                })
            return JsonResponse({
                "ok": False,
                "errors": "username or password is required",
            })
        return JsonResponse({
            "ok": False,
            "error": "phone_number is not correct",
        })
    except IntegrityError:
        return JsonResponse({
            "ok": False,
            "error": "some field is required or username has been used before",
        })
    except AttributeError:
        return JsonResponse({
            "ok": False,
            "error": "username or password is to long",
        })
