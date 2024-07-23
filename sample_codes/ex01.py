from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_utils.plugins.functions import print_result

nr = InitNornir(
      config_file='config.yml'
)
print(nr.inventory.hosts.keys())
print(nr.inventory.hosts.items())
#Access site code of Csw01
print(nr.inventory.hosts['Csw01'].data['site_code'])
print(nr.inventory.groups.keys())
#print(nr.inventory.groups['site1'])
print(nr.inventory.children_of_group('site1'))

for i in nr.inventory.hosts.items():
    print(nr.inventory.hosts[i[0]].data['device_role'])




#output = nr.run(netmiko_send_config, command_string="show ver")
#print(output)