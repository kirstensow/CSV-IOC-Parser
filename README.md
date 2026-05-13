# CSV IOC Parser

A Python tool that reads CSV files containing threat intelligence data, 
extracts and deduplicates IOCs using regex, and exports a clean IOC list 
to a new CSV file.

## Features
- Automatically finds and processes all CSV files in the current directory
- Extracts IOCs by type:
  - IP Addresses
  - Domains
  - MD5 Hashes
- Removes duplicate IOCs using Python sets
- Organises IOCs by type into a dictionary
- Exports clean deduplicated IOC list to CSV

## How to Use
1. Place your CSV files in the same folder as the script
2. Run the script:
```bash
python3 CSVParser.py
```
3. Results are printed to terminal and exported to `IOCs_clean.csv`

## Example Output
IP Address,85.250.54.29
IP Address,192.168.1.105
IP Address,10.0.0.254
Domains,phishing-page.com
Domains,malware-site.com
Hash,5d41402abc4b2a76b9719d911017c592
Hash,7215ee9c7d9dc229d2921a40e899ec5f

## Built With
- Python 3
- re (built-in)
- os (built-in)
