# coding=utf-8
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

#以上为解决python2.7中文编码方案

from django.db import models





# Create your models here.
class User_Info(models.Model):
	uname = models.CharField(max_length=20)
	upwd = models.CharField(max_length=40)
	uemail = models.CharField(max_length=30)
	ushou = models.CharField(max_length=20)
	uaddress = models.CharField(max_length=128, default='')
	uyoubian = models.CharField(max_length=8, default='')
	uphone = models.CharField(max_length=11, default='')
	#default只存在与django界面，不涉及数据库层面
