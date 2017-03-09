#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    return '<h1>Home.</h1>'
	
@app.route('/signin', methods = ['GET'])
def sigin_from():
    return '''<form action= "/signin" method = 'post'>
	          <p><input name = "username"></p>
	          <p><input name = "password" type = "password"></p>
	          <p><button type = "submit">Sign In</p>
			  </form>'''

@app.route('/signin', methods = ['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>username and password are not matching</h3>'

if __name__ == '__main__':
    app.run()