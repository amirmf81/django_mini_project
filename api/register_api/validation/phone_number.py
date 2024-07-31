def validate_phone_number_func(phone_number):
    if phone_number is None:
        return False
    if len(phone_number) != 11:
        return False
    if phone_number[0] == '0' and phone_number[1] == '9':
        return True
    return False
