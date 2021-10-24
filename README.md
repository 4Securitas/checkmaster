# checkmaster
Server or workstation requirements validation tool, configurable, extensible and fast.

## Setup

````
pip install checkmaster
````

## Usage

The parameter `--debug ERROR` will show only the errors and not the entire log
````
checkmaster -c example_conf.json --debug ERROR
````

example of the output
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

Configuration file format conversions
````
checkmaster -c examples/example_conf.yaml --yaml-to-json
checkmaster -c examples/example_conf.json --json-to-yaml
````

Filter which rules to execute by tag

````
checkmaster -c examples/example_conf.json --tags mine
2021-10-24 15:37:32 INFO checkmaster.sockets.ingoing_port {'kind': 'tcp', 'port': 22, 'addrs': ['0.0.0.0'], 'tag': 'mine'}
````


## Configuration file

- json configuration file like [this example](examples/example_conf.json)
- yaml configuration file like [this example](examples/example_conf.yaml)

## Contribute

Feel free to open new issues and pull requests

## For Developers

As you can see each checmaster rule, in the example configuration json file, have a python package and a function name like `checkmaster.sockets.ingoing_port`
 where `checkmaster.sockets` is the python package and the function is `ingoing_port`.

 This means that you can load and use your own `package.function` in checkmaster without any changes in the code!

#### comoiling it for windows


````
sudo apt install wine
wget https://www.python.org/ftp/python/3.7.6/python-3.7.6-amd64.exe
wine python-3.7.6-amd64.exe

wine /home/$USER/.wine/drive_c/users/$USER/Local\ Settings/Application\ Data/Programs/Python/Python37/Scripts/pip install checkmaster pyinstaller
wine /home/$USER/.wine/drive_c/users/$USER/Local\ Settings/Application\ Data/Programs/Python/Python37/Scripts/pyinstaller \
 --hidden-import checkmaster.filesystems \
 --hidden-import checkmaster.distribution \
 --hidden-import checkmaster.hardware \
 --hidden-import checkmaster.sockets \
 --hidden-import checkmaster.commands \
 --paths /home/$USER/.wine/drive_c/users/$USER/Local\ Settings/Application\ Data/Programs/Python/Python37/site-packages /home/$USER/.wine/drive_c/users/$USER/Local\ Settings/Application\ Data/Programs/Python/Python37/Scripts\checkmaster
````

## Authors

- Giuseppe De Marco
- 4Securitas ACSIA Team
