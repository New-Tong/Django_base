# _*_ coding : utf-8 _*_
# @time : 2024/03/14 09:39
# @author : 牛童
# @File : urls.py
# @Project : bookmanage
from django.urls import path
from book.views import index

urlpatterns = [
    path('index/', index),

]
