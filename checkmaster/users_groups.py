import getpass
import os


def user(name=""):
    return name == getpass.getuser()


def uid(name=""):
    return name == os.geteuid()
