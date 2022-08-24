import re 
import os 
import time
from datetime import datetime
from termcolor import colored

print(colored("_"*80, "green"))
print(colored("""
                                             ___                    ___                     ___           ___              
                  ___           ___         /  /\                  /  /\      ___          /__/\         /  /\             
                 /  /\         /__/\       /  /:/_                /  /::\    /  /\         \  \:\       /  /:/_            
  ___     ___   /  /:/         \  \:\     /  /:/ /\              /  /:/\:\  /  /:/          \  \:\     /  /:/ /\           
 /__/\   /  /\ /__/::\          \  \:\   /  /:/ /:/_            /  /:/~/:/ /__/::\      _____\__\:\   /  /:/_/::\          
 \  \:\ /  /:/ \__\/\:\__   ___  \__\:\ /__/:/ /:/ /\          /__/:/ /:/  \__\/\:\__  /__/::::::::\ /__/:/__\/\:\         
  \  \:\  /:/     \  \:\/\ /__/\ |  |:| \  \:\/:/ /:/          \  \:\/:/      \  \:\/\ \  \:\~~\~~\/ \  \:\ /~~/:/         
   \  \:\/:/       \__\::/ \  \:\|  |:|  \  \::/ /:/            \  \::/        \__\::/  \  \:\  ~~~   \  \:\  /:/          
    \  \::/        /__/:/   \  \:\__|:|   \  \:\/:/              \  \:\        /__/:/    \  \:\        \  \:\/:/           
     \__\/         \__\/     \__\::::/     \  \::/                \  \:\       \__\/      \  \:\        \  \::/            
                                 ~~~~       \__\/                  \__\/                   \__\/         \__\/         

By Natnael Kedir 
""","green")) 
print(colored("_"*80, "green")) 

ping_site = input("Specify the website to ping: ")

def ping(ping_site):
    open_pipe = os.popen(f'ping {ping_site}')
    output = open_pipe.read()
    print(f"[+] Ping to {ping_site} sent")
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S")
    with open(f"{ping_site}.txt","a") as opener:
        opener.writelines("\n") 
        opener.writelines("[+] Ping request sent at " + current_time)
        opener.writelines("\n")   
        opener.writelines(output) 
        opener.writelines("-"*80)

def whatismyip(): 
    open_pipe = os.popen('ipconfig')
    output = open_pipe.read()
    myip = re.search('IPv4.*\d',output)
    print(colored("-"*80,"green"))
    print(myip.group(0)) 
    print(colored("-"*80,"green"))

whatismyip() 
while True:
    ping(ping_site)
    time.sleep(1)   