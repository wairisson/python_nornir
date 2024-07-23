from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_config
from jinja2 import Environment, FileSystemLoader

# Inicialize o Nornir
nr = InitNornir(config_file="config.yml")

# Crie um ambiente Jinja para carregar o template
env = Environment(loader=FileSystemLoader("templates/"))

def configurar_hosts(task):
    # Renderize o template Jinja
    template = env.get_template("bgp.j2")
    config = template.render(task.host.data)
    # Envie a configuração usando netmiko_send_config
    task.run(task=netmiko_send_config, config_commands=config.splitlines())
# Filtre os hosts desejados
#hosts = nr.filter(groups="roteadores")
output = nr.run(task=configurar_hosts)

# Imprima o resultado
print_result(output)