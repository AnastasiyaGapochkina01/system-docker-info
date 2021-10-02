#!/usr/bin/python3
import os, platform, subprocess, re, psutil
from jinja2 import Environment, FileSystemLoader
from psutil._common import bytes2human

INCLUDED_PARTITIONS = set(['/', '/etc/hosts'])

def get_system_info():
    system = {
        'cpu_count': psutil.cpu_count(),
        'free_memory': bytes2human(psutil.virtual_memory()[4]),
        'total_memory': bytes2human(psutil.virtual_memory()[0]),
        'disk_usage': []
    }

    partitions = psutil.disk_partitions()
    for p in partitions:
        if p.mountpoint in INCLUDED_PARTITIONS:
                usage = psutil.disk_usage(p.mountpoint)
                system['disk_usage'].append({
                    'mountpoint': p.mountpoint,
                    'total': bytes2human(usage.total),
                    'used': bytes2human(usage.used)
                })
    return system

res = get_system_info()

env = Environment(loader=FileSystemLoader('/opt'))
template = env.get_template('template.html')
html = template.render(page_title='Test job',
                       text_title='Some info about system',
                       cpu=res.get("cpu_count"),
                       total_memory=res.get("total_memory"),
                       free_memory=res.get("free_memory"),
                       disk=res.get("disk_usage"))

with open('system_info.html', 'w') as f:
  f.write(html)