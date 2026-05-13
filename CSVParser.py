import os
import re




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

def organise (ip_match, domain_match, hash_match):
    iocs =  {  #nested dictionary
        'IP Address': ip_match,
        'Domains':domain_match,
        'Hash': hash_match
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







for folders, subfolders, filenames in os.walk(os.getcwd()):

    for filename in filenames:

        if filename.endswith('.csv') and filename != 'IOCs_clean.csv':

            with open(os.path.join(folders, filename), 'r') as file:
                contents = file.read()






            ip_match = ip_address(contents)
            domain_match = domains(contents)
            hash_match = hashes(contents)
            iocs = organise(ip_match, domain_match, hash_match)
            export(iocs)