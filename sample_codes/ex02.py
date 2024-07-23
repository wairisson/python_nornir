from nornir import InitNornir
from nornir_utils.plugins.functions import print_result

def say_hello(task):
    return 'My Task Works! Yaay'

nr = InitNornir(config_file='config.yml')
result = nr.run(task=say_hello)

print_result(result)