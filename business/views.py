from django.shortcuts import render


# Create your views here.
def business_resume(request):
    return render(request, 'business_resume.html')

