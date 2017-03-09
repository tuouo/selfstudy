#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3, os	#sqlite3 inside

path = os.path.join(os.path.abspath('.'), "resource")
conn = sqlite3.connect(os.path.join(path, 'test.db'))	# if not exist, auto create
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values ("1", "tuouo")')
print(cursor.rowcount)			# get numbers of line effected
cursor.close()
conn.commit()
conn.close()

conn = sqlite3.connect(os.path.join(path, 'test.db'))
cursor = conn.cursor()
cursor.execute('select * from user where id = ?', '1')
values = cursor.fetchall()		# result sets(list , line -> trple)
print(values)
cursor.close()
conn.close()
