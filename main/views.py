from django.shortcuts import render

def index(request):
    page_title = "Shkolyar"
    return render(request, 'main/index.html', {'page_title': page_title})

def contact(request):
    return render(request, 'main/contact.html')

def about(request):
    return render(request, 'main/about.html')

def rightholder(request):
    return render(request, 'main/rightholder.html')