from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_config
from nornir_utils.plugins.functions import print_result

def ntp_config(task):
    task.run(task=netmiko_send_config, config_commands=['ntp server 10.10.10.10'])

nr = InitNornir(config_file='config.yml')
results = nr.run(task=ntp_config)

print_result(results)