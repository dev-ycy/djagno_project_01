from django.shortcuts import render, redirect
from django.http import HttpResponse
from emaillist02.models import Emaillist


def index(request):
    results = Emaillist.objects.all().order_by('-id')
    data = {"emaillist_list": results}
    return render(request, 'emaillist02/index.html', data)


def form(request):
    return render(request, 'emaillist02/form.html')



def add(request):
    emaillist = Emaillist()
    emaillist.first_name = request.POST["fn"]
    emaillist.last_name = request.POST["ln"]
    emaillist.email = request.POST["email"]

    emaillist.save()

    return redirect("/emaillist02")
