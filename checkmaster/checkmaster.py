from copy import deepcopy

from . sockets import *
from . filesystems import *
from . commands import *
from . distribution import *
from . hardware import *


logger = logging.getLogger(__name__)


class CheckMaster:
    def __init__(self, conf):
        self.conf = conf
        self.result = deepcopy(conf)

    def check(self):
        self.check_ingoing_ports()

    def run(self, check_name, func):
        for rule in self.result.get(check_name, []):
            _check = func(**rule)
            # _msg = ', '.join([f"{k}: {v}" for k,v in rule.items()])
            msg = f"[{check_name}] - {rule}"
            if not _check:
                logger.error(msg)
            else:
                logger.info(msg)

    def check_ingoing_ports(self):
        self.run('ingoing_ports', check_local_port)
