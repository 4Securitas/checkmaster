# checkmaster
Server assessment tool of requirements like open ports, available commands and stuffs

## Setup

````
pip install checkmaster
````

## Usage

The parameter `--debug ERROR` will show only the errors and not the entire log
````
checkmaster -c example_conf.json --debug ERROR
````

Configuration file format conversions
````
checkmaster -c examples/example_conf.yaml --yaml-to-json
checkmaster -c examples/example_conf.json --json-to-yaml
````


## Configuration file

json configuration file like

````
{
    "checkmaster.sockets.ingoing_port": [
        {"kind": "tcp", "port": 22, "addrs": ["0.0.0.0"]},
        {"kind": "tcp", "port": 8080, "addrs": ["0.0.0.0"]},
        {"kind": "tcp", "port": 8443, "addrs": ["0.0.0.0"]},
        {"kind": "tcp", "port": 80, "status": "CLOSED"},
        {"kind": "tcp", "port": 5044, "addrs": ["0.0.0.0"]},
        {"kind": "udp", "port": 1514},
        {"kind": "tcp", "port": 1515, "addrs": ["0.0.0.0"]}
    ],
    "checkmaster.sockets.outgoing_port": [
        {"addr": "that-host.net", "port":5150, "kind": "tcp", "timeout": 2},
        {"addr": "that-host.net", "port":443, "kind": "tcp", "timeout": 2},
        {"addr": "that-host.net", "port":5986, "kind": "tcp", "timeout": 2},
        {"addr": "that-host.net", "port":22, "kind": "tcp", "timeout": 2}
    ],
    "checkmaster.commands.run": [
        {"cmd": "ping -c 1 google.com", "exit_status":0, "stdout_regexp": "1 received", "stderr_regexp": ""}
    ],

    "checkmaster.hardware.cores": {"operator": "ge", "value": 8},
    "checkmaster.hardware.ram": {"kind": "free",  "operator": "ge", "value": 4, "unit": "GB"},

    "checkmaster.filesystems.size": [
        {"path":"/", "kind":"free", "value":"100", "unit": "GB", "operator":"ge"}
    ],

    "checkmaster.filesystems.paths": [
        {"kind": "file", "path":"./README.md", "status": "present", "permissions": "0664", "uid": 1000, "gid": 1000},
        {"kind": "file", "path":"README.txt", "status": "absent"},
        {"kind": "directory", "path":"READMEs", "status": "absent"}
    ]
}
````

<details>
    <summary>yaml configuration file like ... Click to expand!</summary>

    ````
    checkmaster.commands.run:
    - cmd: ping -c 1 google.com
      exit_status: 0
      stderr_regexp: ''
      stdout_regexp: 1 received
    checkmaster.filesystems.paths:
    - gid: 1000
      kind: file
      path: ./README.md
      permissions: '0664'
      status: present
      uid: 1000
    - kind: file
      path: README.txt
      status: absent
    - kind: directory
      path: READMEs
      status: absent
    checkmaster.filesystems.size:
    - kind: free
      operator: ge
      path: /
      unit: GB
      value: '100'
    checkmaster.hardware.cores:
      operator: ge
      value: 8
    checkmaster.hardware.ram:
      kind: free
      operator: ge
      unit: GB
      value: 4
    checkmaster.sockets.ingoing_port:
    - addrs:
      - 0.0.0.0
      kind: tcp
      port: 22
    - addrs:
      - 0.0.0.0
      kind: tcp
      port: 8080
    - addrs:
      - 0.0.0.0
      kind: tcp
      port: 8443
    - kind: tcp
      port: 80
      status: CLOSED
    - addrs:
      - 0.0.0.0
      kind: tcp
      port: 5044
    - kind: udp
      port: 1514
    - addrs:
      - 0.0.0.0
      kind: tcp
      port: 1515
    checkmaster.sockets.outgoing_port:
    - addr: that-host.net
      kind: tcp
      port: 5150
      timeout: 2
    - addr: that-host.net
      kind: tcp
      port: 443
      timeout: 2
    - addr: that-host.net
      kind: tcp
      port: 5986
      timeout: 2
    - addr: that-host.net
      kind: tcp
      port: 22
      timeout: 2
    ````
</details>

## Contribute

Feel free to open new issues and pull requests

## For Developers

As you can see each checmaster rule, in the example configuration json file, have a python package and a function name like `checkmaster.sockets.ingoing_port`
 where `checkmaster.sockets` is the python package and the function is `ingoing_port`.

 This means that you can load and use your own `package.function` in checkmaster without any changes in the code!

## Authors

- Giuseppe De Marco
- 4Securitas ACSIA Team
