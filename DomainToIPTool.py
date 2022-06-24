#!/usr/bin/env python3


# Created By: Ruben Leonardo Sigalingging.
# Created On: Friday, June 24, 2022, 8:20 PM.
# Function: Convert Website Domain Into IP Address.


def domain_to_ip(created_by="Ruben Leonardo Sigalingging."):
	from os import system
	from pyfiglet import figlet_format
	system("chmod 777 DomainToIPTool.py")
	system("clear")


	tema=figlet_format("Domain",font="slant")
	print(tema)
	print("[!] Created By: Ruben Leonardo Sigalingging.")
	print("[!] Created On: Friday, June 24, 2022, 8:20 PM.")
	print("[!] Function: Convert Website Domain Into IP Address.\n")


	domain=input("[!] Enter Website Domain: ")
	system("ping "+str(domain))
domain_to_ip()