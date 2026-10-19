#create a function that can be reuse, it should show system info
#python -m pip install datetime
#python -m pip install psutil "fastapi[standard]"

import platform
import psutil
import os
import socket
from datetime import datetime

def get_system_details():
    # CPU information
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=True)
    cpu_physical_cores = psutil.cpu_count(logical=False)
    cpu_frequency = psutil.cpu_freq()

    # Memory information
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()

    # Disk information for the root/current drive
    disk = psutil.disk_usage(os.path.abspath(os.sep))

    # Network information
    network = psutil.net_io_counters()

    # System information
    boot_time = datetime.fromtimestamp(psutil.boot_time())

    system_info= {
        
       "System": {
            "Operating System": platform.system(),
            "OS Version": platform.version(),
            "Architecture": platform.machine(),
            "Hostname": socket.gethostname(),
            "Boot Time": boot_time.isoformat(
                timespec="seconds"
            ),
            "Uptime Seconds": int(
                datetime.now().timestamp() - psutil.boot_time()
            ),
        },
        "CPU": {
            "Usage Percent": cpu_percent,
            "Logical Cores": cpu_count,
            "Physical Cores": cpu_physical_cores,
            "Frequency MHz": (
                cpu_frequency.current
                if cpu_frequency else None
            ),
        },
        "Memory": {
            "Total GB": round(memory.total / (1024 ** 3), 2),
            "Available GB": round(memory.available / (1024 ** 3), 2),
            "Used GB": round(memory.used / (1024 ** 3), 2),
            "Usage Percent": memory.percent,
        },
        "Swap": {
            "Total GB": round(swap.total / (1024 ** 3), 2),
            "Used GB": round(swap.used / (1024 ** 3), 2),
            "Usage Percent": swap.percent,
        },
        "Disk": {
            "Total GB": round(disk.total / (1024 ** 3), 2),
            "Used GB": round(disk.used / (1024 ** 3), 2),
            "Free GB": round(disk.free / (1024 ** 3), 2),
            "Usage Percent": disk.percent,
        },
        "Network": {
            "Bytes Sent": network.bytes_sent,
            "Bytes Received": network.bytes_recv,
            "Packets Sent": network.packets_sent,
            "Packets Received": network.packets_recv,
        },
    }
    
    return system_info



