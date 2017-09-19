from django.shortcuts import render, HttpResponse,redirect
from django.utils.crypto import get_random_string
def index(request):
    
    context={
        "string":get_random_string(length=14),
        
    }
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0

    return render(request,'index.html', context)

def generate(request):
    request.session['tries'] += 1  
    return redirect('/')
def reset(request):
    del request.session['tries']
    return redirect('/')
# Create your views here.
