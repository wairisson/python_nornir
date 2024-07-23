from nornir import InitNornir
from nornir_utils.plugins.functions import print_result

nr = InitNornir(config_file="config.yml")

def exibir_variaveis(task):
    variaveis = task.host.data
    print(f"Variáveis do host {task.host.name}:")
    print(variaveis)

hosts = nr.filter(name="Edge01")
resultado = hosts.run(task=exibir_variaveis)
print_result(resultado)