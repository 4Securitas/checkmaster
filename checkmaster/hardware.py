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
    # .virtual_memory() returns all the kind of memory
    # like the following eg. The "kind" parameter selects which one to have
    # svmem(total=16431697920,
          # available=11859709952,
          # percent=27.8,
          # used=3853291520,
          # free=8231968768,
          # active=4153102336,
          # inactive=2009620480,
          # buffers=405647360,
          # cached=3940790272,
          # shared=208187392,
          # slab=581533696
    # )
    res = getattr(psutil.virtual_memory(), kind)
    memory = memory_conv(res, unit)
    logger.debug(f"Found {memory}{unit} {kind} RAM")
    return getattr(op, operator)(memory, value)
