import psutil
import platform
from datetime import datetime, timedelta
import socket
import time

def get_uptime():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.now() - boot_time
    return str(timedelta(seconds=int(uptime.total_seconds())))

def get_system_metrics():
    hostname = socket.gethostname()
    os_version = f"{platform.system()} {platform.release()}"

    cpu_percent = psutil.cpu_percent(interval=1)

    mem = psutil.virtual_memory()
    mem_used = f"{mem.used // (1024 ** 2)} MB"
    mem_total = f"{mem.total // (1024 ** 2)} MB"
    mem_percent = f"{mem.percent}%"

    disk = psutil.disk_usage('/')
    disk_used = f"{disk.used // (1024 ** 3)} GB"
    disk_total = f"{disk.total // (1024 ** 3)} GB"
    disk_percent = f"{disk.percent}%"

    uptime = get_uptime()

    # Return dictionary for app.py to use
    return {
        "hostname": hostname,
        "os_version": os_version,
        "cpu_usage": cpu_percent,
        "memory_used": mem_used,
        "memory_total": mem_total,
        "memory_percent": mem_percent,
        "disk_used": disk_used,
        "disk_total": disk_total,
        "disk_percent": disk_percent,
        "uptime": uptime
    }

if __name__ == "__main__":
    try:
        while True:
            metrics = get_system_metrics()
            print("\n✅ Collected Metrics:")
            for key, value in metrics.items():
                print(f"- {key}: {value}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nStopped metrics monitoring.")
