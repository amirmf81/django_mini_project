from django.http import JsonResponse

from api.register_api.register_api import register_api_func


def register_view_func(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    phone_number = request.POST.get("phone_number")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    gender = request.POST.get("gender")
    national_id_number = request.POST.get("national_id_number")
    birth_date = request.POST.get("birth_date")
    return register_api_func(
        username=username,
        password=password,
        phone_number=phone_number,
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        national_id_number=national_id_number,
        birth_date=birth_date,
    )
