from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def contact(request):
    return render(request, 'main/contact.html')

def about(request):
    return render(request, 'main/about.html')

def rightholder(request):
    return render(request, 'main/rightholder.html')