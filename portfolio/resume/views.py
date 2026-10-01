from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,'resume/index.html',{'email':'amirgodarzy25@gmail.com','name':'amirali godarzy','github':'https://github.com/mell-1101/my_site'})
