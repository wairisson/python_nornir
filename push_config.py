from pathlib import Path
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_napalm.plugins.tasks import napalm_configure
from nornir_napalm.plugins.tasks import napalm_cli 
from nornir_netmiko.tasks import netmiko_send_config
from nornir.core.filter import F
from custom_filters import subnet_filter, host_filter, netmask_filter, ip_filter

nr = InitNornir(config_file="config.yml")


def set_access_sw(task):
    """Render and push configuration to device"""
    # replace template by the device_role content
    rendered_config = task.run(task=template_file, template="ios_access_switch.j2", path="templates/").result
    configure_devices = task.run(task=napalm_configure, dry_run=False, configuration=rendered_config)


def set_core_sw(task):
    """Render and push configuration to device"""
    # replace template by the device_role content
    rendered_config = task.run(task=template_file, template="ios_core_switch.j2", path="templates/").result
    configure_devices = task.run(task=napalm_configure, dry_run=False, configuration=rendered_config)

def set_edge(task):
    """Render and push configuration to device"""
    # replace template by the device_role content
    rendered_config = task.run(task=template_file, template="ios_edge.j2",
                                jinja_filters={"subnet_filter": subnet_filter, "host_filter": host_filter, 'net_filter' : netmask_filter, 'ip_filter' : ip_filter},
                                path="templates/").result
    configure_devices = task.run(task=napalm_configure, dry_run=False, configuration=rendered_config)

def set_filter(site_code, device_role, device_name=None):
    '''
    Apply filter based on Site Code, Device Role, 
    '''
    if site_code and device_role:
        #target = nr.filter(F(site_code__eq='s1') & F(device_role__eq='core_switch'))
        target = nr.filter(F(site_code__eq=site_code) & F(device_role__eq=device_role))

    return target


def main():
    target = nr.filter(F(site_code__eq='s1') & F(host_name__eq='s1-wan-rt01'))
    #target = nr.filter(F(site_code__eq='s1') & F(device_role__eq='wan_router')) 
    result = target.run(task=set_edge)
    #core_sw = nr.filter(F(site_code__eq='s1') & F(device_role__eq='core_switch')) 
    #target = set_filter('s1','core_switch')
    #result = target.run(task=set_core_sw)
    #target = set_filter('s1','access_switch')
    #result = target.run(task=set_access_sw)
    #print(type(result))
    #print_result(result)

    print_result(result)


if __name__ == '__main__':
    main()