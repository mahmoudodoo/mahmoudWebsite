#!/usr/bin/env python3

import os
import socket
import shutil
import psutil
user = os.getenv('USER')



def check_localhost():
        localhost = socket.gethostbyname('localhost')
        return localhost

def check_disk_usage(disk):
        du = shutil.disk_usage(disk)
        free = du.free / du.total * 100
        return free

def check_disk_used(disk):
        du = shutil.disk_usage(disk)
        used = du.used / du.total * 100
        return used


def check_memory_usage():
        mu = psutil.virtual_memory().available
        total = mu / (1024.0 ** 2)
        return total

def check_cpu_usage():
        cu =psutil.cpu_percent(1)
        return cu 

