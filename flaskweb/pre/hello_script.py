#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.script import Manager
# from flask-script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    return '<h1>Hello flask.</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>{name}, Welcome.</h1>'.format(name=name.title())

if __name__ == '__main__':
    manager.run()