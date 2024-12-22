from django.shortcuts import render


def home(request):
    if request.method == "GET":
        return render(request, "catalog/home.html")


def contacts(request):
    if request.method == "GET":
        return render(request, "catalog/contacts.html")
