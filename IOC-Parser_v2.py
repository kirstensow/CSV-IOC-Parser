import os
import re
import json


def ip_address(contents):
    ip_addr = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

    ip_match = ip_addr.findall(contents)

    print('IP Addresses: ' , ip_match)
    return ip_match

def domains (contents):

    domain = re.compile(r'[\w\-]+\.com')

    domain_match = domain.findall(contents)

    print ('Domains: ', domain_match)
    return domain_match

def hashes (contents):

    hash1 = re.compile(r'[0-9a-f]{32}')

    hash_match = hash1.findall(contents)

    print ('Hashes: ' , hash_match)
    return hash_match

def organise(all_ips, all_domains, all_hashes):
    iocs = {
            'IP Address': all_ips,
            'Domains': all_domains,
            'Hash': all_hashes
        }

#Remove Duplicates
    for ioc_type in iocs:
        iocs[ioc_type] = list(set(iocs[ioc_type])) #converts each list to a set (removes duplicates) then back to a list

    print(iocs)
    return iocs

def export(iocs):
    with open('IOCs_clean.csv', 'w') as file:
        for ioc_type, indicators in iocs.items():
            for indicator in indicators:
                file.write(f'{ioc_type},{indicator}\n')


all_ips = []
all_domains = []
all_hashes = []



for folders, subfolders, filenames in os.walk(os.getcwd()):

    for filename in filenames:

        if filename.endswith('.csv') and filename != 'IOCs_clean.csv': #Reads contents from csv

            with open(os.path.join(folders, filename), 'r') as file:
                contents = file.read()

        elif filename.endswith('.json'): #Reads contents from json
            with open(os.path.join(folders, filename), 'r') as file:
                data = json.load(file)
                contents = json.dumps(data)  # convert back to string for regex


        elif filename.endswith('.txt'): #Reads contents from text files
            with open(os.path.join(folders, filename), 'r') as file:
                contents = file.read()

        # runs after each file regardless of type, adds them to empty lists
        all_ips.extend(ip_address(contents))
        all_domains.extend(domains(contents))
        all_hashes.extend(hashes(contents))

iocs = organise(all_ips, all_domains, all_hashes) #Passes liss to be organised
export(iocs) #List exported as csv file
