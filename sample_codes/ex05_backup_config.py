from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.tasks.files import write_file

def backup_config(task):
    output = task.run(task=netmiko_send_command, command_string='show run')
    task.run(task=write_file, filename=f'{task.host}-backup.cfg', content=output[0].result)

nr = InitNornir(config_file='config.yml')
results = nr.run(task=backup_config)