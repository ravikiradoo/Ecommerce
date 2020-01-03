def  get_client_ip(request):
    ip =""
    x_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_for:
        ip = x_for.split(",")[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    return ip