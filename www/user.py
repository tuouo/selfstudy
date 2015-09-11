#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from orm import Model, StringField, IntegerField
class User(Model):
    __tables__ = 'users'
    id = IntegerField(primary_key = True)
    name = StringField()

user = User(id = 123, name = 'tuouo')
user.insert()
users = User.findAll()