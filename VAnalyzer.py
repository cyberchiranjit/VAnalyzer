#!/usr/bin/env/python3

import sys
import os
import time
from myfunction import whatwebb, nmap_in, dirb, nikto_scan, nslookup, dig

os.system("clear")

class colors:
    RED = "\33[91m"
    FIN = "\033[0m"
    BLUE = "\33[94m"
    
banner = """    
 ______________________________________________________________________________
            __     ___                _                    
            \ \   / / \   _ __   __ _| |_   _ _______ _ __ 
             \ \ / / _ \ | '_ \ / _` | | | | |_  / _ \ '__|
              \ V / ___ \| | | | (_| | | |_| |/ /  __/ |   
               \_/_/   \_\_| |_|\__,_|_|\__, /___\___|_|   
                                        |___/      v 0.1                               
|______________________________________________________________________________|
|                                                                              |
|                                                                              |
|                                                                              |
|                 User Name:          [ cyberchiranjit ]                       |
|                                                                              |
|                 Password:           [ *************  ]                       |
|                                                                              |
|                                                                              |
|                                                                              |
|                                [ LOGIN ]                                     |
|______________________________________________________________________________|
|                                                                              |
|                                                   Instagram: @cyberchiranjit |
|______________________________________________________________________________|

"""

for clr in banner:
    print(colors.RED + clr, end="")
    sys.stdout.flush()
    time.sleep(0.0015)

line = "\n"
for clr in line:
    print(colors.FIN + clr, end="")
    sys.stdout.flush()
    time.sleep(0.5)
    
# Ask for Continue or Exit the script
def ask():
    print("\n")
    ask = str(input(colors.BLUE + "Do you want to continue(c) or exit?(e) : "))   
    if ask == "c":
        for i in range(1):
            print("\n")
            continue
    else:
        print("Bye!! ^__^")
        sys.exit()

while True:

    def main_page():
        print("\n")
        print(colors.RED + "1.  DNS Information")
        print(colors.FIN + "2.  NMAP Scan")
        print(colors.RED + "3.  Whois Scan")
        print(colors.FIN + "4.  Identify technologies used by websites")
        print(colors.RED + "5.  Find the directories of a website")
        print(colors.FIN + "6.  Nikto Scan")
        print(colors.RED + "7.  Download Wordlist for Discovering Sub-Domains")
        print(colors.FIN + "8.  NsLookup")
        print(colors.RED + "9.  My Methodology")        
        print(colors.FIN + "10. Exit")
        print("\n")
        global take_option
        take_option = int(input("Choose the option: "))
            
    main_page()

    if take_option == 1:
        take_input = input("Enter the URL: ")
        print("\n")
        print("="*80)
        print("                    ", "DNS Information", "               ")
        print("_"*80)
        os.system("dig {}".format(take_input))
        print("="*80)
        ask()

    elif take_option == 2:
        print("\n")
        print("1.  Intense Scan")
        print("2.  Intense scan plus UDP")
        print("3.  Intense scan, all TCP ports")
        print("4.  Intense scan, no ping")
        print("5.  Ping Scan")  
        print("6.  Quick scan")
        print("7.  Quick scan plus")
        print("8.  Quick traceroute")
        print("9.  Regular scan")
        print("10. Slow comprehensive scan")
        print("11. Specific port scan")
        print("12. Back")
        print("13. Exit")
        
        print("\n")
         
        scan = int(input("Choose the scan type: "))
        
        if scan == 1:
            take_input = input("Enter the URL: ")
            print("\n")
            print("="*80)
            print("              NMAP Scan: Intense Scan           ")
            print("_"*80)
            print("\n")
            os.system("nmap -T4 -A -v {}".format(take_input))
            print("="*80)
            ask()
        
        elif scan == 2:
            take_input = input("Enter the URL: ")
            print("\n")
            print("="*80)
            print("              NMAP Scan: Intense scan plus UDP           ")
            print("_"*80)
            print("\n")
            os.system("nmap -sS -sU -T4 -A -v {}".format(take_input))
            print("="*80) 
            ask()   
                
        elif scan == 3:
            take_input = input("Enter the URL: ")
            print("\n")
            print("="*80)
            print("              NMAP Scan: Intense scan, all TCP ports          ")
            print("_"*80)
            print("\n")
            os.system("nmap -sS -sU -T4 -A -v {}".format(take_input))
            print("="*80)
            ask()
            
        elif scan == 4:
            take_input = input("Enter the URL: ")
            print("\n")
            print("="*80)
            print("              NMAP Scan: Intense scan, no ping           ")
            print("_"*80)
            print("\n")
            os.system("nmap -T4 -A -v -Pn {}".format(take_input))
            print("="*80) 
            ask()
            
        elif scan == 5:
            take_input = input("Enter the URL: ")
            print("\n")
            print("="*80)
            print("              NMAP Scan: Ping scan          ")
            print("_"*80)
            print("\n")
            os.system("nmap -sn {}".format(take_input))
            print("="*80) 
            ask()
            
        elif scan == 6:
            take_input = input("Enter the URL: ")
            print("\n")
            print("="*80)
            print("              NMAP Scan: Quick scan            ")
            print("_"*80)
            print("\n")
            os.system("nmap -T4 -F {}".format(take_input))
            print("="*80) 
            ask()
            
        elif scan == 7:
            take_input = input("Enter the URL: ")
            print("\n")
            print("="*80)
            print("              NMAP Scan: Quick scan plus           ")
            print("_"*80)
            print("\n")
            os.system("nmap -sV -T4 -O -F --version-light {}".format(take_input))
            print("="*80) 
            ask()
            
        elif scan == 8:
            take_input = input("Enter the URL: ")
            print("\n")
            print("="*80)
            print("              NMAP Scan: Quick traceroute          ")
            print("_"*80)
            print("\n")
            os.system("nmap -sn --traceroute {}".format(take_input))
            print("="*80) 
            ask()
           
        elif scan == 9:
            take_input = input("Enter the URL: ")
            print("\n")
            print("="*80)
            print("              NMAP Scan: Regular scan          ")
            print("_"*80)
            print("\n")
            os.system("nmap {}".format(take_input))
            print("="*80) 
            ask()
           
        elif scan == 10:
            take_input = input("Enter the URL: ")
            print("\n")
            print("="*80)
            print("              NMAP Scan: Slow comprehensive scan          ")
            print("_"*80)
            print("\n")
            os.system('nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53 --script "default or (discovery and safe)" {}'.format(take_input))
            print("="*80) 
            ask()
            
        elif scan == 11:
            take_input = input("Enter the URL: ")
            ports = input("Enter the ports [1-100 or 23,445,80]: ")
            ask_os = str(input("Enable OS detection, version detection, script scanning, and traceroute [y | n]? :"))
            print("\n")
            print("="*80)
            print("              NMAP Scan: Slow comprehensive scan          ")
            print("_"*80)
            print("\n")
            if ask_os == "y":
                os.system('nmap -T4 -p {} -A {}'.format(ports, take_input))
            else:
                os.system('nmap -T4 -p {} {}'.format(ports, take_input))
            print("="*80) 
            ask()            
            
        elif scan == 12:
            print("\n")
            continue
            
        elif scan == 13:
            print("\n")
            sys.exit()
                
    elif take_option == 3:        
        take_input = input("Enter the URL: ")
        take_input = os.popen('ping -c 1 www.chiranjitofficial.tk | grep "64 bytes" | cut -d " " -f 5 | tr -d "():"').read()
        print("\n")
        print("="*80)
        print("                      Whois Scan                   ")
        print("_"*80)
        print("\n")
        os.system('whois {}'.format(take_input))
        print("="*80) 
        ask()                
    
    elif take_option == 4:
        take_input = input("Enter the URL: ")
        print("\n")
        print("="*80)
        print("                 Identify technologies used by websites              ")
        print("_"*80)
        print("\n")
        todo = os.popen('whatweb -v -a 3 {}'.format(take_input)).read()
        output_split_comma = todo.split(",")
        for i in output_split_comma:
            print(i)
            sys.stdout.flush()
            time.sleep(0.02)
        print("="*80)
        ask()                 



    elif take_option == 5:
        take_input = input("Enter the URL [https://www.test.com/ or http://www.test.com/]: ")
        wordlist = input("Enter path of the wordlist: ")
        print("\n")
        print("="*80)
        print("              Scannig for Directories (Dirb)              ")
        print("_"*80)
        print("\n")
        os.system('dirb {} {}'.format(take_input, wordlist))
        print("="*80) 
        ask()
        
    elif take_option == 6:
        take_input = input("Enter the URL: ")
        print("\n")
        print("="*80)
        print("              Nikto Scan              ")
        print("_"*80)
        print("\n")
        os.system('nikto -h {}'.format(take_input))
        print("="*80) 
        ask()        
    
    elif take_option == 7:
        print("\n")
        print("1. Small Wordlist")
        print("2. Medium Wordlist")
        print("3. Large Wordlist")
        print("4. Back")
        print("5. Exit")
        print("\n")
        option = int(input("Enter your choice: "))
        if option == 1:
            print("\n")
            print("="*80)
            print("              Download Wordlist for Finding Sub-Domains : Small              ")
            print("_"*80)
            print("\n")
            os.system("curl -o small_sub_domain_wordlist.txt https://raw.githubusercontent.com/cyberchiranjit/subdomains/master/small_subdomains-100.txt")
            print("="*80)
            print("\n")
            print(colors.RED + "[!] Saved in the current directy")
            ask()
            
        elif option == 2:
            print("\n")
            print("="*80)
            print("              Download Wordlist for Finding Sub-Domains : Medium              ")
            print("_"*80)
            print("\n")            
            os.system("curl -o medium_sub_domain_wordlist.txt https://raw.githubusercontent.com/cyberchiranjit/subdomains/master/medium_subdomains-500.txt")
            print("="*80)
            print("\n")
            print(colors.RED + "[!] Saved in the current directy")            
            ask()
            
        elif option == 3:
            print("\n")
            print("="*80)
            print("              Download Wordlist for Finding Sub-Domains : Large             ")
            print("_"*80)
            print("\n")
            os.system("curl -o large_sub_domain_wordlist.txt https://raw.githubusercontent.com/cyberchiranjit/subdomains/master/large_subdomains-10000.txt")
            print("\n")
            print("\n")
            print(colors.RED + "[!] Saved in the current directy")            
            ask()
            
        elif option == 4:
            for i in range(1):
                continue
                
        elif option == 5:
            print("Bye *__* !!")
            sys.exit()
            
        else:
            print("Learn 1 2 3 first then use this script!! Lol")
    
    elif take_option == 8:
        take_input = input("Enter the URL: ")
        print("\n")
        print("="*80)
        print("             NsLookup            ")
        print("_"*80)
        print("\n")
        os.system('nslookup {}'.format(take_input))
        print("="*80) 
        ask()         

    elif take_option == 9:
        take_input_http = input("Enter the URL [https://www.test.com] : ")
        if "https" in take_input_http:
            if take_input_http[-1] == "/":
                take_input_http = take_input_http[0:-1]                 
            take_input = take_input.replace("https://www." ,"")
        elif "http" in take_input_http:
            if take_input_http[-1] == "/":
                take_input_http = take_input_http[0:-1]            
            take_input = take_input.replace("http://www." ,"")
        wordlist = input("Enter path of the wordlist: ")     
        print("\n")
        print("="*80)
        print("               MY METHODOLOGY                ")
        print("-"*80)
        print("\n")
        print("-"*80)
        print("I'm sure you noted the In-Scope domains :)")
        print("-"*80)
        print("\n")
        dig(take_input)
        nslookup(take_input)
        whatwebb(take_input)
        curl(take_input)
        nmap_in(take_input)
        dirb(take_input_http, wordlist)        
        nikto_scan(take_input)
    
    elif take_option == 10:
        print("Bye!! ^__^")
        sys.exit()
        
