import logging
import operator as op
import psutil

logger = logging.getLogger(__name__)


def memory_conv(res, unit, **kwargs) -> int:
    if unit.lower() == "gb":
        res = ((res / 1024) / 1024) / 1024
    elif unit.lower() == "mb":
        res = (res / 1024) / 1024
    elif unit.lower() == "kb":
        res = res / 1024
    return round(res, 2)


def cores(operator="ge", value=0, **kwargs) -> int:
    """
    see https://docs.python.org/3/library/operator.html
    """
    cores = psutil.cpu_count()
    logger.debug(f"Found {cores} CPU cores")
    return getattr(op, operator)(cores, value)


def ram(unit="MB", kind="free", operator="ge", value=0, **kwargs) -> int:
    """
    kind = [
         'active',
         'available',
         'buffers',
         'cached',
         'count',
         'free',
         'inactive',
         'index',
         'percent',
         'shared',
         'slab',
         'total',
         'used'
    ]
    """
    # total physical memory available usually in Bytes
    res = getattr(psutil.virtual_memory(), kind)
    memory = memory_conv(res, unit)
    logger.debug(f"Found {memory}{unit} {kind} RAM")
    return getattr(op, operator)(memory, value)
