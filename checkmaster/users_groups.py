import getpass
import os
import subprocess


def user(name="", **kwargs):
    return name == getpass.getuser()


def uid(name="", **kwargs):
    return name == os.geteuid()


def passwordless_sudo(cmd="", proof="OK", **kwargs):
    cmd = cmd or "echo OK"
    args = f"sudo -n -S {cmd} 2>/dev/null".split()
    kwargs = dict(stdout=subprocess.PIPE)
    cmd = subprocess.run(args, **kwargs)
    return proof in str(cmd.stdout)
