from ipaddress import IPv4Interface
import ipaddress


def subnet_filter(supernet, p_len, s_number):
    """
    It takes a supernet, a subnet len and subnet number 
    and returns subnet corresponding.
    Ex:
    subnet_filter(10.0.0.0/24, 30, 1)
    return the fist 10.0.0.4/30 
    """
    prefix = ipaddress.ip_network(supernet)
    subnet = list(prefix.subnets(new_prefix=p_len))
    return subnet[s_number]

def host_filter(network, h_number):
    """
    It takes a supernet, a subnet len and subnet number 
    and returns subnet corresponding.
    Ex:
    subnet_filter(10.0.0.0/24, 30, 1)
    return the fist 10.0.0.4/30 
    """
    #prefix = list(ip_network('192.0.2.0/29').hosts())
    prefix = ipaddress.ip_network(network)
    host_ips = list(prefix.hosts())
    return host_ips[h_number]

def ip_filter(ip_network):
    """
    It takes an IP network and returns the IP address

    :param ip_network: The IP address and subnet mask in CIDR notation
    :return: The IP address of the interface.
    """
    return IPv4Interface(ip_network).ip


def netmask_filter(ip_network):
    """
    It takes an IP network in CIDR notation and returns the netmask

    :param ip_network: The IP address and subnet mask in CIDR notation
    :return: The netmask of the ip_network
    """
    return IPv4Interface(ip_network).netmask