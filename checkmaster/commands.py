import re
import logging
import subprocess

logger = logging.getLogger(__name__)


def run(cmd, exit_status=0, stdout_regexp=None, stderr_regexp=None, **kwargs) -> bool:
    # subprocess.CompletedProcess
    res = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    logger.debug(logger)
    if not res.returncode == exit_status:
        return False
    elif stdout_regexp and not re.findall(stdout_regexp, res.stdout.decode()):
        return False
    elif stderr_regexp and not re.findall(stderr_regexp, res.stderr.decode()):
        return False

    return True
