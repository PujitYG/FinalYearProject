from django.shortcuts import render

# Create your views here.



def error(request):
    return render(request,'error_404/404.html')