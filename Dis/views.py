from wsgiref.simple_server import ServerHandler

from django.shortcuts import render, HttpResponse, redirect, reverse
from Dis import models
# Create your views here.
import os
from django import forms


class ResForm(forms.Form):
    username = forms.CharField(label='用户名:')
    name = forms.CharField(label='真是姓名:')
    phone = forms.CharField(label='手机号码:')
    password = forms.CharField(label='密码:')
    re_password = forms.CharField(label='确认密码:')


def register(request):
    form_obj = ResForm()
    if request.method == 'POST':
        form_obj = ResForm(data=request.POST)
    return render(request, 'register.html', {'form_obj': form_obj})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('loginUsername')
        pwd = request.POST.get('loginPassword')
        obj = models.User.objects.filter(username=username, password=pwd)
        if obj:
            return redirect(reverse('tables'))

    return render(request, 'login.html')


def charts(request):
    return render(request, 'charts.html')


def index(request):
    return render(request, 'index1.html')


def home(request):
    return render(request, 'home.html')


# 展示全部的数据
def tables(request):
    obj = models.Pictures.objects.all()
    return render(request, 'table.html', {'dic': obj})


def mobile(request):
    obj = models.Pictures.objects.filter(type='phone')
    return render(request, 'tablep.html', {'dic': obj})


def computer(request):
    obj = models.Pictures.objects.filter(type='PC')
    return render(request, 'tabled.html', {'dic': obj})


def modal(request,pk):
    obj = models.Pictures.objects.filter(type='PC', pk=pk)
    return render(request, 'mt.html',{'dic':obj})
def modal1(request,pk):
    obj = models.Pictures.objects.filter(type='PC', pk=pk)
    return render(request, 'mt1.html',{'dic':obj})

def details(request):
    return render(request, 'details.html', {'dic': 1})


# 图片上传
def uploadps(request):
    if request.method == 'GET':
        return render(request, 'uploadps.html')
    elif request.method == 'POST':
        # 1.获取上传的图片文件
        imgfile = request.FILES.get('img',None)
        imgfile1 = request.FILES.get('img1',None)
        if not imgfile:
            return HttpResponse("no files for upload!")
            # ret = imgfile.size #文件大小    做文件上传大小限制
        # imgfile.content_type 文件类型  做文件上传类型限制
        res = imgfile.name #文件名称
        res1 = imgfile1.name #文件名称
        r_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_p = os.path.join(r_path,'static','pictures','d')
        path_p1 = os.path.join(r_path,'static','pictures','z')
        with open('{}/{}'.format(path_p,res),'wb') as f:
            for chunk in imgfile.chunks():
                f.write(chunk)
        with open('{}/{}'.format(path_p1, res1), 'wb') as f:
            for chunk in imgfile.chunks():
                f.write(chunk)
        # 2.创建数据模型对象
        # print(r_path)
        img = models.Pictures.objects.create()
        # u = 'pictures/d/' + res
        u = '../../static/pictures/d/' + res
        # u1 = 'pictures/z/'+res1
        u1 = '../../static/pictures/z/' + res1

        img.url = u
        img.url1 = u1
        # # 3.保存
        img.save()
        # path = '../../static/pictures/d' + '图片名称'
        return redirect(reverse('tables'))


def pictur(request, pk):
    obj = models.Pictures.objects.filter(type='phone', pk=pk)
    # obj1 = models.Videos.objects.filter((type='phone'))
    if not obj:
        pass
    return render(request, 'picture.html', {'dic': obj})
def pictur1(request, pk):
    obj = models.Pictures.objects.filter(type='PC', pk=pk)
    # obj1 = models.Videos.objects.filter((type='phone'))
    if not obj:
        pass
    return render(request, 'picture1.html', {'dic': obj})

def forms(request):
    return render(request, 'forms.html')


def test(request):
    ret = models.User.objects.all()
    print(ret, type(ret))
    # for i in ret:
    #     print(i.username)

    return render(request, 'test.html', {'ret': ret})


def upload(request):
    if request.method == 'POST':
        res = request.POST.get('username')
        ret = request.POST.get('picture')

        obj = request.FILES.get('picture')
        print(obj.name, obj.size)
        print(res)
    return render(request, 'upload.html')
