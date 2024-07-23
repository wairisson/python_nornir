from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_napalm.plugins.tasks import napalm_cli 
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command
from nornir.core.filter import F
from rich import print

def send_netmiko_cmd(task,cmd):
    task.host.platform = 'cisco_ios'
    configure_devices = task.run(task=netmiko_send_command, command_string=cmd )


def send_sh_cmd(task,cmd):
    #plataforma = task.host.platform
    #print(plataforma)
    configure_devices = task.run(task=napalm_cli, commands =[cmd])


def main():
    nr = InitNornir(config_file="config.yml")
    
    # filter switches from site s1
    #core_sw = nr.filter(F(site_code__eq='s1') & F(device_role__eq='core_switch')) 
    core_sw = nr.filter(F(site_code__eq='s1') & F(host_name__eq='s1-wan-rt01'))
   # core_sw = nr.filter(F(site_code__eq='s1') & F(device_role__eq='wan_router')) 
    output = core_sw.run(task=send_netmiko_cmd,cmd='sh ip int br')
    print(type(output))
    print_result(output)


if __name__ == '__main__':
    main()