import importlib
import logging

from copy import deepcopy

logger = logging.getLogger(__name__)


class CheckMaster:
    def __init__(self, conf, log_style = 'label', tags=None):
        self.conf = conf
        self.result = deepcopy(conf)
        self.tags = tags
        self.log_style = log_style

    def load_plugin(self, plugin_name):
        n1, _, n2 = plugin_name.rpartition(".")
        module = importlib.import_module(n1)
        func = getattr(module, n2)
        return func

    def _check(self, func_name, func, rule, tags):
        if self.tags and rule.get('tag') not in tags:
            return

        _check = func(**rule)
        if self.log_style == 'label':
            msg = f"{rule.get('label') or rule}"
        else:
            msg = f"{func_name} {rule}"
        if not _check:
            logger.error(msg)
        else:
            logger.info(msg)

    def start(self):
        for _func, rules in self.result.items():
            func = self.load_plugin(_func)
            if isinstance(rules, dict):
                self._check(_func, func, rules, self.tags)
            elif isinstance(rules, list):
                for rule in rules:
                    self._check(_func, func, rule, self.tags)
            else:
                raise NotImplemented(_func)
