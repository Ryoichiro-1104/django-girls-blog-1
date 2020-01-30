from django.shortcuts import render

# Create your views here.
def list(request):
    if request.method == "GET":
        context = {"message":"Index"}
    elif request.method == "POST":
        context = {"message":"Create"}
    return render(request,"hello.html",context)