import dns.resolver
import socket
from colorama import Fore, init

init()

dns_record = {}

website = input(Fore.LIGHTBLUE_EX + "Entrez l'url de votre site: ")

try:
    a_record = dns.resolver.resolve(website, 'A')
    for ipval in a_record:
        dns_record[Fore.LIGHTYELLOW_EX + 'IP'] = ipval.to_text()

    mx_record_list = []

    mx_record = dns.resolver.resolve(website,'MX')
    for server in mx_record:
        mx_record_list.append(server)
    for i, element in enumerate(mx_record_list):
        dns_record['DNS', i+1] = element

    print (Fore.GREEN + f'Hostname: {website}')

    for key,value in dns_record.items():
        print(Fore.LIGHTCYAN_EX +  f"{key} = {value}")

except socket.gaierror as error:
    print (f"Invalide Hostname, l'erreur est {error}")    
