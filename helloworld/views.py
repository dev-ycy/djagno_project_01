from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, 'helloworld/main.html')
    
def hello1(request):
    return HttpResponse("ok!", content_type='text/html; charset=utf-8')

def hello2(request):
    return render(request, 'helloworld/hello2.html')

def tags(request):
    return render(request, 'helloworld/tags.html')

def form(request):
    return render(request, 'helloworld/form.html')

    
def join(request):
    # GET 이라는 딕셔너리에 key는 email, value는 값을 받아오는 개념
    # email = request.GET['email']
    # password = request.GET['password']
    return render(request, 'helloworld/join.html')