#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello flask.</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>{name}, Welcome.</h1>'.format(name=name.title())

if __name__ == '__main__':
    app.run(debug = True)