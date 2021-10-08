import distro
import platform as pf

from multiprocessing import cpu_count


def get_architecture() -> str:
    """example: x86_64"""
    return pf.architecture()

def get_processor() -> str:
    """example: x86_64"""
    return pf.processor()

def get_platform() -> str:
    """Linux-5.4.0-88-generic-x86_64-with-glibc2.29"""
    return pf.platform()

def get_system() -> str:
    """example: Linux"""
    return pf.system()

def get_linux_kernel() -> str:
    """example: 5.4.0-88-generic"""
    return pf.release()

def get_system() -> str:
    """example: Linux"""
    return pf.system()

def get_system() -> str:
    """example: Linux"""
    return pf.system()

def get_distro() -> dict:
    """example: Linux"""
    return {
        'base': distro.like(),
        'name': distro.id(),
        'codename': distro.codename(),
        'version': distro.version(),
    }
