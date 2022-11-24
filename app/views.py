from django.shortcuts import render

# Create your views here.
def fun(request):
    d={'name':'sasank','age':21}
    return render(request,'fun.html',d)