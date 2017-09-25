#coding=utf-8
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

#以上为路径带有中文的编码解决方案

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from models import *
from hashlib import sha1

# Create your views here.
def register(request):
	return render(request,'df_user/register.html')
	print ('register')

def register_handle(request):
	#接受用户输入
	post = request.POST
	uname = post.get('user_name')
	upwd = post.get('pwd')
	upwd2 = post.get('cpwd')
	uemail = post.get('email')
	#判断两次密码
	if upwd != upwd2:
		return redirect('/user/register/')
	else:
		#密码加密
		s1 = sha1()
		s1.update(upwd)
		upwd3 = s1.hexdigest()
		user = User_Info()
		user.uname = uname
		user.upwd = upwd3
		user.uemail = uemail
		user.save()
		return redirect('/user/login/')


def register_exist(request):
	name = request.GET.get('name')
	ucount = User_Info.objects.filter(uname = name).count()
	return JsonResponse('count':ucount)