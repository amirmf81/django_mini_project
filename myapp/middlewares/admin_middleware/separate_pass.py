def separate_path_func(request):
    if "admin/" in request.path:
        return False
    return True
