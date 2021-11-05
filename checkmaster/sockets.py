import logging
import psutil
import socket

LOCAL_ADDRESS = ["127.0.0.1", "0.0.0.0", "::"]
logger = logging.getLogger(__name__)


def ingoing_port(
    port, status="LISTEN", kind="tcp", addrs=LOCAL_ADDRESS, **kwargs
) -> bool:
    """
    +------------+----------------------------------------------------+
    | Kind Value | Connections using                                  |
    +------------+----------------------------------------------------+
    | inet       | IPv4 and IPv6                                      |
    | inet4      | IPv4                                               |
    | inet6      | IPv6                                               |
    | tcp        | TCP                                                |
    | tcp4       | TCP over IPv4                                      |
    | tcp6       | TCP over IPv6                                      |
    | udp        | UDP                                                |
    | udp4       | UDP over IPv4                                      |
    | udp6       | UDP over IPv6                                      |
    | unix       | UNIX socket (both UDP and TCP protocols)           |
    | all        | the sum of all the possible families and protocols |
    +------------+----------------------------------------------------+
    """
    for i in psutil.net_connections(kind=kind):
        logger.debug(i)
        result = all(
            (i.status == status, i.laddr.ip in addrs, i.laddr.port == port))
        if result:
            return result
        else:
            result = False

    if not result and status in ["CLOSED", "NA"]:
        return True
    return result


def outgoing_port(addr, port, timeout=4, kind=None, **kwargs) -> bool:
    # TODO: kind is unused !!!
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((addr, int(port)))
        s.shutdown(2)
        return True
    except Exception:
        return False
