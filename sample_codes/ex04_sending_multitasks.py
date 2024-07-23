from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result

def get_output(task):
    task.run(task=netmiko_send_command, command_string='show ip interface brief | excl down')
    task.run(task=netmiko_send_command, command_string='show ip arp')

nr = InitNornir(config_file='config.yml')
results = nr.run(task=get_output)

print_result(results)

'''
task.run - This is used within a task function to execute another task. Think of it as calling a 
sub-task within your main task. When you use task.run, you're essentially saying,
 "While performing this task, go ahead and run these additional tasks as part of it."
nr.run - On the other hand, nr.run is used to kick off tasks at the top level. This is the method
 you call when you want to start your automation process and execute tasks across your inventory of devices.
'''