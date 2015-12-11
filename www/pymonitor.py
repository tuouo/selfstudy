#!/usr/bin/envpython3
# -*- coding: utf-8 -*-
import os, sys, time, subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def log(message):
    print()