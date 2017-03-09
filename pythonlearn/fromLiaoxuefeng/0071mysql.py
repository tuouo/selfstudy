#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import mysql.connector

# mysql service must start before this program run.
# or can't connect

# pip install mysql-connector-python --allow-external mysql-connector-python

conn = mysql.connector.connect(user = 'root', password = '', database = 'test')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values(%s, %s)', ['1', 'tuouo'])		# %
print("rowcount = ", cursor.rowcount)
conn.commit()					# don't forget
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ['1'])
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()