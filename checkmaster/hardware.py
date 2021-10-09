import psutil


def memory_conv(res, unit) -> int:
    if unit.lower() == "gb":
        res = ((res / 1024) / 1024) / 1024
    elif unit.lower() == "mb":
        res =  (res / 1024) / 1024
    elif unit.lower() == "kb":
        res = res / 1024
    return int(res)

def get_cpus() -> int:
    return cpu_count()

def get_ram(unit="MB", kind='free') -> int:
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
    res = getattr(psutil.virtual_memory(), kind)  # total physical memory available in Bytes
    return memory_conv(res, unit)
