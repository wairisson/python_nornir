from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
import getpass

nr = InitNornir(config_file='config.yml')
username = getpass.getpass('Please enter the username:')
password = getpass.getpass('Please enter the password:')


nr.inventory.groups['cisco'].username = username
nr.inventory.groups['cisco'].password = password


results = nr.run(task=netmiko_send_command, command_string='show ip arp')
print_result(results)
