from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>INDEX SAYFASI</h1>")

def about(request):
    return render(request, 'about.html')