import distro as dist
import getpass
import os
import logging
import psutil
import requests
import socket

from .hardware import memory_conv

logger = logging.getLogger(__name__)

# note from Stefan: worth to check between IPv4 and IPv6 that icanhazip.com provides.
def get_ips(url="https://icanhazip.com/"):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(4)
    s.connect(("8.8.8.8", 80))
    _ip = s.getsockname()[0]
    _hostn = socket.gethostbyaddr(_ip)

    ips = {
        "public ip": requests.get(url).content.decode().strip(),
        "private ip": _ip,
        "private hostname": _hostn[0],
        "other private ips": print(", ".join(_hostn[1] if len(_hostn) > 1 else [])),
    }
    return ips


def get_distro_info():
    values = {
        "base": dist.like(),
        "name": dist.id(),
        "codename": dist.codename(),
        "version": dist.version(),
        "cores": psutil.cpu_count(),
        "free_ram": memory_conv(psutil.virtual_memory().free, unit="gb"),
        "user": getpass.getuser(),
    }
    try:
        values["uid"] = os.geteuid()
    except Exception as e:
        pass
    return values


def sockets_processes_names():
    res = {}

    for i in psutil.net_connections():
        _proc = psutil.Process(i.pid)
        _name = _proc.name()
        logger.debug(_proc)
        data = dict(
            pid=_proc.pid,
            exe=_proc.exe(),
            process_name=_name,
            port=i.laddr.port,
            bind=i.laddr.ip,
        )
        if _name in res:
            res[_name].append(data)
        else:
            res[_name] = [data]
    return res
