import logging
import operator as op
import os
import psutil

from datetime import datetime

from checkmaster.hardware import memory_conv

logger = logging.getLogger(__name__)


def paths(
    path, kind="file", status="present", permissions=None, uid=None, gid=None, **kwargs
):
    if kind == "file":
        _func = os.path.isfile
    elif kind == "directory":
        _func = os.path.isdir

    try:
        exists = _func(path)
    except FileNotFoundError:
        if status != "present":
            return True
        else:
            return False

    # existence
    if exists and status == "present":
        status = True
    elif not exists and status == "absent":
        return True
    elif not exists and status == "present":
        return False
    else:
        raise NotImplementedError()

    # permissions
    if permissions or uid or gid:
        try:
            perms = get_permissions(path)
            logger.debug(perms)
        except FileNotFoundError as e:
            logger.error(e)
            return False
    else:
        return status

    # TODO: additional checks on atime, ctime, mtime are possible
    if permissions and permissions != perms["permissions"]:
        return False
    elif uid and uid != perms["user"]:
        return False
    elif gid and gid != perms["group"]:
        return False
    else:
        return status


def get_permissions(path) -> dict:
    """example: 0o100664"""
    st = os.stat(path)
    perm = str(oct(st.st_mode))
    return {
        "raw_permissions": perm,
        "permissions": perm[4:],
        "user": st.st_uid,
        "group": st.st_gid,
        "create": datetime.fromtimestamp(st.st_ctime),
        "modified": datetime.fromtimestamp(st.st_mtime),
        "last_access": datetime.fromtimestamp(st.st_atime),
    }


def size(path, unit="MB", kind="free", operator="ge", value=100, **kwargs) -> int:
    """
    kind = set(
        total, used, free, percent
    )
    """
    size = psutil.disk_usage(path)
    if kind == "percent":
        size = size.percent
    else:
        size = memory_conv(getattr(size, kind), unit)
    value = float(value)
    logger.debug(f"Found {size}{unit} in {path}")
    return getattr(op, operator)(size, value)


def current_working_directory(path, **kwargs):
    return path == os.getcwd()
