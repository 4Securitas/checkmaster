# checkmaster
Server assessment tool of requirements like open ports, available commands and stuffs

## Setup

````
pip install checkmaster
````

## Usage

````
checkmaster -c example_conf.json
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
    "ingoing_ports": [
        {"kind": "tcp", "port": 22, "location": "0.0.0.0"},
        {"kind": "tcp", "port": 8080, "location": "0.0.0.0"},
        {"kind": "tcp", "port": 8443, "location": "0.0.0.0"},
        {"kind": "tcp", "port": 80, "status": "CLOSED"},
        {"kind": "tcp", "port": 5044, "location": "0.0.0.0"},
        {"kind": "udp", "port": 1514},
        {"kind": "tcp", "port": 1515, "location": "0.0.0.0"}
    ],
    "outgoing_ports": [
        {"addr": "that-host.net", "port":5150, "kind": "tcp"},
        {"addr": "that-host.net", "port":443, "kind": "tcp"},
        {"addr": "that-host.net", "port":5986, "kind": "tcp"},
        {"addr": "that-host.net", "port":22, "kind": "tcp"}
    ],

    "system_commands": [
        {"cmd": "ping -c 1 google.com", "exit_status":0, "stdout_regexp": "1 received", "stderr_regexp": ""}
    ],

    "cpu": {"core_min": 8},
    "ram": {"free_min": "7GB"},

    "filesystems": [
        {"path":"/", "free_min": "100GB"}
    ],

    "paths": [
        {"kind": "file", "path":"./README.md", "status": "present", "permissions": "0664"},
        {"kind": "file", "path":"README.txt", "status": "absent", "uid": 1000},
        {"kind": "directory", "path":"READMEs", "status": "absent"}
    ]
}
````


yaml configuration file like

````
cpu:
  core_min: 8
filesystems:
- free_min: 100GB
  path: /
ingoing_ports:
- kind: tcp
  location: 0.0.0.0
  port: 22
- kind: tcp
  location: 0.0.0.0
  port: 8080
- kind: tcp
  location: 0.0.0.0
  port: 8443
- kind: tcp
  port: 80
  status: CLOSED
- kind: tcp
  location: 0.0.0.0
  port: 5044
- kind: udp
  port: 1514
- kind: tcp
  location: 0.0.0.0
  port: 1515
outgoing_ports:
- addr: that-host.net
  kind: tcp
  port: 5150
- addr: that-host.net
  kind: tcp
  port: 443
- addr: that-host.net
  kind: tcp
  port: 5986
- addr: that-host.net
  kind: tcp
  port: 22
paths:
- kind: file
  path: ./README.md
  status: present
- kind: file
  path: README.txt
  status: absent
- kind: directory
  path: READMEs
  status: absent
ram:
  free_min: 7GB
system_commands:
- cmd: ping -c 1 google.com
  exit_status: 0
  stderr_regexp: ''
  stdout_regexp: 1 received
````

## Authors

- Giuseppe De Marco
- 4Securitas ACSIA Team
