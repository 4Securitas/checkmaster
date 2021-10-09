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

def get_ram(unit="MB") -> int:
    res = psutil.virtual_memory().total  # total physical memory available in Bytes
    return memory_conv(res, unit)
