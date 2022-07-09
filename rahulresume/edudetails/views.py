from django.shortcuts import render
from .models import Edudetails

# Create your views here.
def details(request):
    det=Edudetails.objects.all()
    return render(request , 'edudetails/details.html',{'det':det})
