from django.shortcuts import render, redirect
from .models import Guestbook


def index(request):
    results = Guestbook.objects.all().order_by('-regdate')
    data = {
        "guestbook_list": results # guestbook_list 구성 = [{},{}] 형태 (리스트 안 딕셔너리 형태)
    }

    return render(request, 'guestbook02/index.html', data)



def add(request):
    guestbook = Guestbook() # 객체를 먼저 만들기
    guestbook.name = request.POST["name"]
    guestbook.password = request.POST["password"]
    guestbook.message = request.POST["message"]
    # 원칙은, 받아오는 데이터 인증작업 해야함.

    guestbook.save()

    return redirect("/guestbook02")


def deleteform(request): # request 안에 두개? 넘겨서 옴 (no, password?)
    return render(request, 'guestbook02/deleteform.html')


def delete(request):
    # id = request.POST['id']
    # password = request.POST["password"]

    guestbook = Guestbook.objects.filter(id=request.POST['id']).filter(password=request.POST["password"])
    guestbook.delete()

    return redirect("/guestbook02")