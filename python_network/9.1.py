import pprint

access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}


def generate_access_config(access_config, access_mode_template, port_security=None):
    intf_dict= {}
    for interface, vlan in access_config.items():
        commands = []
        for command in access_mode_template:
            if "vlan" in command:
                commands.append(f"{command} {vlan}")
            else:
                commands.append(command)
        if port_security:
            for command in port_security:
                commands.append(command)
        intf_dict[interface] = commands
        
    return intf_dict

pprint.pprint(generate_access_config(access_config, access_mode_template, port_security_template))

