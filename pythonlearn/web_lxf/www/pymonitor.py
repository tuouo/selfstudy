#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, time, subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


process = None
command = ['echo', 'ok']
def log(message):
    print("[monitor]: %s" % message)


class MyFileSystemEventHander(FileSystemEventHandler):
    def __init__(self, fn):
        super(MyFileSystemEventHander, self).__init__()
        self.restart = fn

    def forEvveryEvent(self, event):
        if event.src_path.endswith('.py'):
            log("Python source:%s changed." % event.src_path)
            self.restart()


def kill_process():
    global process
    if process:
        log("kill process--%s" % process.pid)
        process.kill()
        process.wait()
        log("Process ended with '%s'" % process.returncode)
    process = None

def start_process():
    global process, command
    log("*** start process %s ***" % ' '.join(command))
    process = subprocess.Popen(command, stdin = sys.stdin, stdout = sys.stdout, stderr = sys.stderr, shell = True)

def restart_process():
    kill_process()
    start_process()


def watch(path, callback):
    observer = Observer()
    observer.schedule(MyFileSystemEventHander(restart_process), path, recursive = True)
    observer.start()
    log("*** watching directory %s ***" % path)
    start_process()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    argv = sys.argv[1:]
    if not argv:
        print("exit.")
        exit(0)
    command = argv
    watch(os.path.abspath('.'), None)