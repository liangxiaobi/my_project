# coding:utf-8
'''
Created on 2013-2-20

@author: lion
'''
from django.contrib import admin
from django.db import models

class Person(models.Model):
    name = models.CharField('作者姓名', max_length=10)
    age = models.IntegerField('作者年龄')
    def __unicode__(self):
        return self.name
    
admin.site.register(Person)

class Book(models.Model):
    person = models.ForeignKey(Person, related_name='person_book')
    title = models.CharField('书籍名称', max_length=10)
    pubtime = models.DateField('出版时间')
    
    def __unicode__(self):
        return self.title
    
    
admin.site.register(Book)