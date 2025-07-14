import functions_framework

@functions_framework.http
def hello_http(request):
    return "{products: {cold_cat: 100, hot_dog: 99, uwu:50}}"
