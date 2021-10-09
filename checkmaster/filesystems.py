import os


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
        'permissions': perm[4:],
        'user': st.st_uid,
        'group': st.st_gid,
        'create': st.st_ctime,
        'modified': st.st_mtime,
        'last_access': st.st_atime
    }
