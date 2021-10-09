import os
import psutil
from datetime import datetime

from checkmaster.hardware import memory_conv


def file_exists(path):
    return os.path.isfile(path)

def dir_exists(path):
    return os.path.isdir(path)

def get_permissions(path):
    """example: 0o100664"""
    st = os.stat(path)
    perm = str(oct(st.st_mode))
    return {
        'raw_permissions': perm,
        'permissions': perm[3:],
        'user': st.st_uid,
        'group': st.st_gid,
        'create': datetime.fromtimestamp(st.st_ctime),
        'modified': datetime.fromtimestamp(st.st_mtime),
        'last_access': datetime.fromtimestamp(st.st_atime)
    }

def get_free_space(path, unit='MB', kind='free') -> int:
    """
        kind = set(
            total, used, free, percent
        )
    """
    size = psutil.disk_usage(path)
    if kind == 'percent':
        return size.percent
    else:
        return memory_conv(getattr(size, kind), unit)
