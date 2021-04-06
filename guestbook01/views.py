from django.shortcuts import render, redirect
from . import models

# Create your views here.

def index(request):
    results = models.findall()
    data = {
        "guestbook_list": results # guestbook_list 구성 = [{},{}] 형태 (리스트 안 딕셔너리 형태)
    }

    return render(request, 'guestbook01/index.html', data)


def add(request):
    name = request.POST["name"]
    password = request.POST["password"]
    message = request.POST["message"]

    models.insert(name, password, message)

    return redirect("/guestbook01")


def deleteform(request): # request 안에 두개? 넘겨서 옴 (no, password?)
    # no = request.GET["no"]
    # data = {
    #     'no': no
    #     }
    return render(request, 'guestbook01/deleteform.html')


def delete(request):
    # 비번 같으면 모델에서 지우고, 리스트로 redirect 
    # 해당 no 어떻게 받아오지?
    no = request.POST['no']
    password = request.POST["password"]

    models.deleteby_no_and_password(no, password)
   
    return redirect("/guestbook01")

