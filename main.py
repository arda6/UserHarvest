
import requests
from bs4 import BeautifulSoup as bs

ip2 = requests.get("https://ip-adresim.net/")
source = bs(ip2.content,"lxml")
head2 = source.find("strong",attrs={"class","mycurrentip"})
rem2 = head2.text
ips = rem2.split()
print("""

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░████████░░██░░░░░████░░░░░██░░░██░░░░░
░░░░░░░░░░██░░██░░░░██░░██░░░░██░░██░░░░░░
░░░░░░░░░██░░░██░░░██░░░░██░░░██░██░░░░░░░
░░░░░░░░██░░░░██░░██░░░░░░██░░████░░░░░░░░
░░░░░░░██░░░░░██░░██████████░░██░░██░░░░░░
░░░░░░██░░░░░░██░░██░░░░░░██░░██░░░██░░░░░
░░░░░██░░░░░░░██░░██░░░░░░██░░██░░░██░░░░░
░░░░████████░░██░░██░░░░░░██░░██░░░██░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░0x47░░░0x4F░░░0x4B░░░0x43░░░0x45░░░░░


 """)

def remote():
    adress = input("{#} Set UserName  {#} ")

    print("\n<IP> Your IP Adress  " +ips[0]+" </IP>\n")
    
    ip = requests.get("https://www.instagram.com/"+adress+"/",timeout=5 ,headers={"User-Agent":"Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"})
    aas = ip.content
    aa = str(aas)
    son = aa.find("Followers")
    if son != -1 and ip.status_code == 200:
        print("/+\ UserName "+adress+" Found /+\ ")
    elif son == -1 and ip.status_code == 404:   
        print("/-\ UserName "+adress+" Not Found /-\ ")


remote()
