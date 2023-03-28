# checkmaster
Quick validation tool to check the prerequisites for a typical Server or workstation; configurable, extensible and fast.


![CI build](https://github.com/4Securitas/checkmaster/workflows/checkmaster/badge.svg)
![License](https://img.shields.io/badge/license-Affero%203-blue)
![Python version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue.svg)
[![Downloads](https://pepy.tech/badge/checkmaster)](https://pepy.tech/project/checkmaster)
[![Downloads](https://pepy.tech/badge/checkmaster/week)](https://pepy.tech/project/checkmaster)

## Setup

````
yum install python3 python3-devel
# OR
apt install python3 python3-dev

pip install checkmaster
````

## Usage

If executed without a configuration file, checkmaster returns some general information on the specific environment where it's been executed.

````
{
  "base": "debian",
  "name": "ubuntu",
  "codename": "jammy",
  "version": "22.04",
  "cores": 16,
  "free_ram": 20.43,
  "user": "wert",
  "uid": 1000,
  "public ip": "153.50.22.250",
  "private ip": "192.168.0.65",
  "private hostname": "pro.hub",
  "other private ips": "",
  "other private ipv6": [
    "::1",
    "fe80::686:1117:8a81:4015",
    "fe80::42:f4ff:fe30:6622",
    "fe80::dcac:dcff:fe33:3bbc"
  ]
}
````

Adding the parameter `--debug ERROR` will show only errors and not the all logs.
````
checkmaster -c example_conf.json --debug ERROR --log-style raw
````

Example of checkmaster output with only errors:
````
ERROR checkmaster.sockets.ingoing_port {'kind': 'tcp', 'port': 8080, 'addrs': ['0.0.0.0']}
ERROR checkmaster.sockets.ingoing_port {'kind': 'tcp', 'port': 8443, 'addrs': ['0.0.0.0']}
ERROR checkmaster.sockets.ingoing_port {'kind': 'tcp', 'port': 5044, 'addrs': ['0.0.0.0']}
ERROR checkmaster.sockets.ingoing_port {'kind': 'udp', 'port': 1514}
ERROR checkmaster.sockets.ingoing_port {'kind': 'tcp', 'port': 1515, 'addrs': ['0.0.0.0']}
ERROR checkmaster.sockets.outgoing_port {'addr': 'that-host.net', 'port': 5150, 'kind': 'tcp', 'timeout': 2}
ERROR checkmaster.sockets.outgoing_port {'addr': 'that-host.net', 'port': 443, 'kind': 'tcp', 'timeout': 2}
ERROR checkmaster.sockets.outgoing_port {'addr': 'that-host.net', 'port': 5986, 'kind': 'tcp', 'timeout': 2}
ERROR checkmaster.sockets.outgoing_port {'addr': 'that-host.net', 'port': 22, 'kind': 'tcp', 'timeout': 2}
````

Normal checkmaster output:
![image](https://user-images.githubusercontent.com/1297620/139543038-fc8622f8-e238-43f9-ad87-488ad38c7168.png)


To convert the configuration file format:
````
checkmaster -c examples/example_conf.yaml --yaml-to-json
checkmaster -c examples/example_conf.json --json-to-yaml
````

To filter by rules on the execution tag basis:

````
checkmaster -c examples/example_conf.json --tags mine
2021-10-24 15:37:32 INFO checkmaster.sockets.ingoing_port {'kind': 'tcp', 'port': 22, 'addrs': ['0.0.0.0'], 'tag': 'mine'}
````


## Configuration file

- Example json configuration file: [this example](examples/example_conf.json)
- Example yaml configuration file: [this example](examples/example_conf.yaml)

## Contribute

Open to contribution, please feel free to open new issues and pull requests.

## For Developers

As you can see each checkmaster rule in the example configuration json file, has a python package and a function named something like `checkmaster.sockets.ingoing_port` where `checkmaster.sockets` is the python package and the function is `ingoing_port`.

This means that you can use your custom `package.function` and load into checkmaster without performing any changes on the checkmaster code!

#### Compiling checkmaster

 - [PyInstaller for Windows](PYINSTALLER-WIN.md)
 - [NUITKA](NUITKA.md)


## Authors

- Giuseppe De Marco
- 4Securitas ACSIA Team
