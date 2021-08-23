import requests
import json
from termcolor import colored
print(colored(""" 
print("[+] ----------------tüfekcireal----------------------[+]")
print("[-] Author : TÜFEKCİREAL ")
print("[-] GİT HUB : https://github.com/tufekcireal ")
print("[-] İNSTAGRAM : https://instagram.com/tufekcireal")
print("[-] YOU TUBE : Bir Coder ")
print("[+] ----------------TUFEKCİREAL----------------------[+]")
print("[+] ----------------TUFEKCİREAL----------------------[+]")                     
""" , "green"))
from ipdata.cli import ip

ip_adress = input(colored("IP: " , "red"))

response = requests.get(f'http://ip-api.com/json/{ip_adress}').content

data = json.loads(response)

print(colored(f"""
IP: {data['query']}
Country: {data['country']}
City: {data['city']}
ISP: {data['isp']}
ZIP: {data['zip']}
Lon: {data['lon']}
LAT: {data['lat']}
""" , "yellow"))