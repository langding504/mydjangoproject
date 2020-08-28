from django.shortcuts import render


def index(request):
    context = {
        'page_title':'Selamat Datang di LangDing',
    }
    return render(request,'index.html',context)