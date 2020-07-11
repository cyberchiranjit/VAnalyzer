import os

def whatwebb(take_input):
    print("\n")
    print("="*80)
    print("                 Identify technologies used by websites              ")
    print("_"*80)
    print("\n")
    todo = os.popen('whatweb -v -a 3 {}'.format(take_input)).read()
    output_split_comma = todo.split(",")
    for i in output_split_comma:
        print(i)
    print("="*80)
    
def nmap_in(take_input):
    print("\n")
    print("="*80)
    print("              NMAP Scan: Intense scan, all TCP ports          ")
    print("_"*80)
    print("\n")
    os.system("nmap -sS -sU -T4 -A -v {}".format(take_input))
    print("="*80)
    
def dirb(take_input_http, wordlist):
    print("\n")
    print("="*80)
    print("              Scannig for Directories (Dirb)              ")
    print("_"*80)
    print("\n")
    os.system('dirb {} {}'.format(take_input_http, wordlist))
    print("="*80)
    
def down_word():
    print("\n")
    print("1. Small Wordlist")
    print("2. Medium Wordlist")
    print("3. Large Wordlist")
    print("\n")
    option = int(input("Enter your choice: "))
    print("\n")
    print("="*80)
    print("              Download Wordlist for Finding Sub-Domains               ")
    print("_"*80)
    print("\n")
    if option == 1:
        os.system("curl -o small_sub_domain_wordlist.txt <link>")
    elif option == 2:
        os.system("curl -o medium_sub_domain_wordlist.txt <link>")
    elif option == 3:
        os.system("curl -o large_sub_domain_wordlist.txt <link>")
    else:
        print("Learn 1 2 3 first then use this script!! Lol")
    print("="*80)

def dig(take_input):
    print("\n")
    print("="*80)
    print("                    ", "DNS Information", "               ")
    print("_"*80)
    os.system("dig {}".format(take_input))
    print("="*80)    

def nikto_scan(take_input):
    print("\n")
    print("="*80)
    print("                 Nikto Scan                 ")
    print("_"*80)
    print("\n")
    os.system("nikto -h {}".format(take_input))
    print("="*80) 
    
def nslookup(take_input): 
    print("\n")
    print("="*80)
    print("             NsLookup            ")
    print("_"*80)
    print("\n")
    os.system('nslookup {}'.format(take_input))
    print("="*80)
