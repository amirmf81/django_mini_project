from django.http import JsonResponse

from myapp.middlewares.admin_middleware.separate_pass import separate_path_func
from myapp.models.user_model import User


class AdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if separate_path_func(request=request):
            return self.get_response(request)
        if not User.check_admin(request.POST.get("username")):
            return JsonResponse({
                "ok": False,
                "error": "you dont have access",
            }, status=403)
        return self.get_response(request)
