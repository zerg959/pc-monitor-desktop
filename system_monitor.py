import psutil
import time


def get_sys_info():
    cpu_percentage = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return {
        'cpu_percent': cpu_percentage,
        'ram_percent': ram.percent,
        'ram_used': ram.used / (1024**3),
        'ram_total': ram.total / (1024**3),
        'disk_percent': disk.percent,
        'disk_used': disk.used / (1024**3),
        'disk_total': disk.total / (1024**3),
        'time': time.strftime("%Y-%m-%d %H:%M:%S")
    }
