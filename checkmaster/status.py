import distro as dist
import getpass
import os
import logging
import netifaces
import psutil
import requests
import socket

from .hardware import memory_conv

logger = logging.getLogger(__name__)


# note from Stefan: worth to check between IPv4 and IPv6 that icanhazip.com provides.
def get_ips(url: str = "https://icanhazip.com/", timeout: int = 4) -> dict:
    # ipv4
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(timeout)
    s.connect(("8.8.8.8", 80))
    _ip = s.getsockname()[0]
    ips = {
        "public ip": requests.get(url, timeout=timeout).content.decode().strip(),
        "private ip": _ip,
    }

    try:
        _hostn = socket.gethostbyaddr(_ip)
        ips["private hostname"] = _hostn[0]
        ips["other private ips"] = []
        for i in netifaces.interfaces():
            addrs = netifaces.ifaddresses(i)
            has_ipv6 = addrs.get(netifaces.AF_INET)
            if has_ipv6:
                for ii in has_ipv6:
                    _addr = ii["addr"]
                    if "%" in _addr:
                        _addr = _addr.split("%")[0]
                    ips["other private ips"].append(_addr)
    except socket.herror as e:
        logger.warning(f"get_ips error: {e}")
    except Exception as e:
        logger.warning(f"get_ips error: {e}")

    return ips


def get_ips_v6(url: str = "https://icanhazip.com/", timeout: int = 4) -> dict:
    # ipv6
    try:
        s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        s.settimeout(timeout)
        s.connect(("2a00:1450:4002:406::2003", 80))
        _ip = s.getsockname()[0]
        ips = {
            "public ipv6": requests.get(url, timeout=timeout).content.decode().strip(),
            "private ipv6": _ip,
        }
    except OSError as e:
        logger.warning(f"IPV6 routing failed: {e}")
        ips = {}

    ips["other private ipv6"] = []

    for i in netifaces.interfaces():
        addrs = netifaces.ifaddresses(i)
        has_ipv6 = addrs.get(netifaces.AF_INET6)
        if has_ipv6:
            for ii in has_ipv6:
                _addr = ii["addr"]
                if "%" in _addr:
                    _addr = _addr.split("%")[0]
                ips["other private ipv6"].append(_addr)

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
        logger.warning(f"get_distro_info error: {e}")
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
