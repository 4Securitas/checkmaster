import distro as dist
import logging
import platform as pf

from multiprocessing import cpu_count

logger = logging.getLogger(__name__)


def architecture(kind, **kwargs) -> str:
    """example: ('64bit', 'ELF')"""
    return kind == pf.architecture()

def processor(kind, **kwargs) -> str:
    """example: x86_64"""
    return kind == pf.processor()

def platform(kind, **kwargs) -> str:
    """Linux-5.4.0-88-generic-x86_64-with-glibc2.29"""
    return kind == pf.platform()

def system(kind, **kwargs) -> str:
    """example: Linux"""
    return kind == pf.system()

def linux_kernel(kind, **kwargs) -> str:
    """example: 5.4.0-88-generic"""
    return kind == pf.release()

def system(kind, **kwargs) -> str:
    """example: Linux"""
    return kind == pf.system()

def distro(**kwargs) -> dict:
    """example: Linux"""
    values = {
        'base': dist.like(),
        'name': dist.id(),
        'codename': dist.codename(),
        'version': dist.version(),
    }

    for i in kwargs:
        if i not in values:
            logger.warning(f'{i} is not a valid distribution attribute')
        if kwargs[i].lower() != values[i].lower():
            return False
    return True
