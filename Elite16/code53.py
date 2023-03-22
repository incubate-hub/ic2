#95 write a program to Remove leading zeros from an IP address

import re
def removeLeadingZeros(ip):
    modified_ip = re.sub(regex, '.', ip)
    print(modified_ip)


if __name__ == '__main__' : 
	
	ip = "216.08.094.196"
	removeLeadingZeros(ip)