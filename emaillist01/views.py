from django.shortcuts import render
from emaillist01 import models
from django.shortcuts import redirect

def index(request):
    results = models.findall()
    data = {
        "emaillist_list": results #emaillist_list 구성 = [{},{}] 형태 (리스트 안 딕셔너리 형태)
    }
    return render(request, 'emaillist01/index.html', data)


def form(request):
    return render(request, 'emaillist01/form.html')


def add(request):
    firstname = request.POST["fn"]
    lastname = request.POST["ln"]
    email = request.POST["email"]

    models.insert(firstname, lastname, email)

    return redirect("/emaillist01")
