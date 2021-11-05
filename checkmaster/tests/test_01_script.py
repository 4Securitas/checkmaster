import os

CMD = "checkmaster"


def test_base() -> int:
    print(CMD)
    assert not os.system(CMD)

def test_example() -> int:
    """
    must fail
    """
    assert os.system(f"{CMD} -c ../examples/example_conf.json")
