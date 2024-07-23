from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result


nr = InitNornir(config_file='config.yml')


results_ip_brief = nr.run(task=netmiko_send_command, command_string='show ip interface brief | excl down')
results_ip_arp = nr.run(task=netmiko_send_command, command_string='show ip arp')


print_result(results_ip_brief)
print_result(results_ip_arp)