#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os, sqlite3

db_file = os.path.join(os.path.abspath('.'), 'resource', 'test.db')
db_file = os.path.join(os.path.dirname(__file__), 'resource', 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)
	
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute("insert into user values ('A001', 'Lily', 89)")
cursor.execute("insert into user values ('A002', 'Mack', 93)")
cursor.execute("insert into user values ('A003', 'Dick', 83)")
cursor.execute("insert into user values ('A004', 'Mo', 82)")
cursor.execute("insert into user values ('A005', 'Tu', 73)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("select name from user where score between ? and ? order by score", (low, high))
    values = cursor.fetchall()
    #print(values)
    cursor.close()
    conn.close()
    names = []
    for i in values:
         names.append(i[0])
    return names
	
assert get_score_in(85, 95) == ['Lily', 'Mack'], get_score_in(85, 95)
assert get_score_in(65, 80) == ['Tu'], get_score_in(65, 80)
assert get_score_in(65, 100) == ['Tu', 'Mo', 'Dick', 'Lily', 'Mack'], get_score_in(65, 100)
assert get_score_in(65, 66) == [], get_score_in(65, 66)
print("OK")