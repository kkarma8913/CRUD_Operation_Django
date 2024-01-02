from django.http import HttpResponse

def display(request):
    return HttpResponse('<h1>Helooo this is my first page</h1>')
