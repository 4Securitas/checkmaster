# checkmaster
Server or workstation requirements validation tool, configurable, extensible and fast.

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

If executed without any cofniguration file, checkmaster returns some general information about the environment where it have been executed

````
{
  "base": "debian",
  "name": "ubuntu",
  "codename": "focal",
  "version": "20.04",
  "public ip": "151.53.91.70",
  "private ip": "192.168.3.115",
  "private hostname": "wert-desktop.that-thing.lan",
  "other private ips": null
}
````

The parameter `--debug ERROR` will show only the errors and not the entire log
````
checkmaster -c example_conf.json --debug ERROR --log-style raw
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

normal output
![image](https://user-images.githubusercontent.com/1297620/139543038-fc8622f8-e238-43f9-ad87-488ad38c7168.png)


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

#### Compiling it for Windows


````
sudo apt install wine
wget https://www.python.org/ftp/python/3.7.6/python-3.7.6-amd64.exe
wine msiexec /i python-3.7.6-amd64.exe /qb

wine /home/$USER/.wine/drive_c/users/$USER/Local\ Settings/Application\ Data/Programs/Python/Python37/Scripts/pip install checkmaster pyinstaller
wine /home/$USER/.wine/drive_c/users/$USER/Local\ Settings/Application\ Data/Programs/Python/Python37/Scripts/pyinstaller \
 -F --clean \
 --hidden-import checkmaster.filesystems \
 --hidden-import checkmaster.distribution \
 --hidden-import checkmaster.hardware \
 --hidden-import checkmaster.sockets \
 --hidden-import checkmaster.commands \
 --paths /home/$USER/.wine/drive_c/users/$USER/Local\ Settings/Application\ Data/Programs/Python/Python37/site-packages /home/$USER/.wine/drive_c/users/$USER/Local\ Settings/Application\ Data/Programs/Python/Python37/Scripts/checkmaster
````

Unfortunately VirtusTotal have false positive with the previous compilation, so

````
pip uninstall pyinstaller
````
Then download and install [VS Cpp Community Edition](http://visualstudio.microsoft.com/vs/features/cplusplus/).
Download [pyInstaller package](http://github.com/pyinstaller/pyinstaller/releases) and unzip it in `C:\Pyinstaller`

then
````
cd C:\Pyinstaller\bootloader
python ./waf all --target-arch=64bit

set PYPATH="c:\users\utente\appdata\local\packages\pythonsoftwarefoundation.python.3.9_qbz5n2kfra8p0\localcache\roaming\python\python39"

pyinstaller -F --hidden-import checkmaster.filesystems --hidden-import checkmaster.distribution --hidden-import checkmaster.hardware --hidden-import checkmaster.sockets --hidden-import checkmaster.commands --paths $PYPATH\site-packages $PYPATH\\Scripts\checkmaster
````

if you still have false positive from virus total consider to notify your checkmaster.exe to antivirus vendors!


## Authors

- Giuseppe De Marco
- 4Securitas ACSIA Team
