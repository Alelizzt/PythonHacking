#!/usr/bin/python

import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous','anonymous')
        print "[+] " + hostname + " FTP anonymous Succeded! "
        ftp.quit()
        return True
    except Exception, e:
        print "[-] " + hostname + "FTP anonymous Failed."


host = raw_input("Enter the IP address: ")
anonLogin(host)
