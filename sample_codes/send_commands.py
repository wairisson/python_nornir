from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_napalm.plugins.tasks import napalm_cli 
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command
from nornir.core.filter import F
from rich import print
import json

def send_netmiko_cmd(task,cmd):
    task.host.platform = 'cisco_ios'
    #print(task.host.name)
    configure_devices = task.run(task=netmiko_send_command,  command_string=cmd, use_textfsm=True )#.result
    #print(type(configure_devices))
    #print(configure_devices)
    
    #return configure_devices
    #return json.dumps(configure_devices, indent=2)
    #for neighbor in configure_devices:
    #    neighbor_state = neighbor['state']
    #    print(task.host.platform, '-- Results')
    #    print(f"Estado do vizinho {neighbor['neighbor_id']}: {neighbor_state}")

def main():
    nr = InitNornir(config_file="config.yml")
    core_sw = nr.filter(F(site_code__eq='s1') & F(host_name__eq='s1-wan-rt01'))   # core_sw = nr.filter(F(site_code__eq='s1') & F(device_role__eq='wan_router')) 
    result = core_sw.run(task=send_netmiko_cmd,cmd='show ip ospf nei')
    #print(type(result))
    #print(output.result.items())
    print(result)
    print(result['Edge01'])
    print(result['Edge01'][1])
    print(result['Edge01'][1].result)
    var =  result['Edge01'][1].result
    print(type(var))
    print(var[0]['neighbor_id'])
    print(var[0]['state'])
    print(var[0]['interface'])

    
    
    #for i in result.items():
    #    print(i)
        #return:
        #('Edge01', MultiResult: [Result: "send_netmiko_cmd", Result: "netmiko_send_command"])
    #print(result['Edge01'][1])
    #for i in result['Edge01']:
    #    print(i)
    #    print(type(i.result))
        #var = list(i.result)
        #print(var)
        #print(json.dumps(i.result, indent=2))
        #print(i.result[0])


if __name__ == '__main__':
    main()