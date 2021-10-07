# checkmaster
Server assessment tool of requirements like open ports, available commands and stuffs


## Configuration file

json file like

````
{
    'ingoing_ports': [
        {'kind': 'tcp', 'port': 22},
        {'kind': 'udp', 'port': 53},
        {'kind': 'tcp', 'port': 80, status='CLOSED'},

    ],
    'outgoing_ports': [
        {'addr': "that-host.net", "port":443, "kind": "tcp"}
    ],

    "system_commands": [
        {"cmd": 'ping -c 1 google.com', "exit_status":0, stdout_regexp: "1 received", stderr_regexp: ""}
    ],

    "memory": {"free_min": 100000},

    "filesystems": [
        {"path":"/", "free_min":100000},
    ],

    "paths": [
        {"kind": 'file', "path":"./README.md", "status"="present"},
        {"kind": 'file', "path":"README.txt", "status"="absent"},
        {"kind": 'directory', "path":"READMEs", "status"="absent"},
    ],



}
````
