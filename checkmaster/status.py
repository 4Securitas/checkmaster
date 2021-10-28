import distro as dist
import requests
import socket


def get_ips(url="https://icanhazip.com/"):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(4)
    s.connect(("8.8.8.8", 80))
    _ip = s.getsockname()[0]
    _hostn = socket.gethostbyaddr(_ip)

    ips = {
        'public ip': requests.get(url).content.decode().strip(),
        'private ip': _ip,
        'private hostname': _hostn[0],
        'other private ips': print(", ".join(_hostn[1] if len(_hostn)>1 else []))
    }
    return ips


def get_distro_info():
    values = {
        'base': dist.like(),
        'name': dist.id(),
        'codename': dist.codename(),
        'version': dist.version(),
    }
    return values

