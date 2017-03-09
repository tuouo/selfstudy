#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello flask.</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>{name}, Welcome.</h1>'.format(name=name.title())

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>{name}, Welcome.</h1>'.format(name=user.name)

@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return '<h1>You browser is {browser}</h1>'.format(browser=user_agent)

@app.route('/bad')
def bad():
    return '<h1>Bad Request.</h1>', 400

@app.route('/setcookie')
def setcookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/redirect')
def redirect():
    return redirect("http://www.example.com")


if __name__ == '__main__':
    app.run(debug = True)