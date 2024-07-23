
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir.core.filter import F
def get_output(task):
    print(task.host)
    task.run(task=netmiko_send_command, command_string='show ip interface brief | excl down')
    task.run(task=netmiko_send_command, command_string='show ip arp')


nr = InitNornir(config_file='config.yml')
# manda comando para todo inventario
#results = nr.run(task=get_output)

# Instancia Nornir para 1 host especifico
#target = nr.filter(name="Edge02")
#target = nr.filter(F(name__eq='Edge02'))

target = nr.filter(F(site_code__eq='s10') & F(host_name__eq='s10-edge1'))
result = target.run(task=get_output)
print_result(result)
print('--* '*50)
# Instancia Nornir para 1 host especifico
#group_target = 'cisco'
#send_to_group = nr.filter(F(groups__eq='cisco'))
#result = send_to_group.run(task=get_output)
#print_result(result)

#nr.filter(~F(platform__eq="junos") | ~F(platform_eq="ios"))