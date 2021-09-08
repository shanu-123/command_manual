#!/usr/bin/python3

import sys 
import json

print(sys.argv)
def help_msg():
	print("Wrong option")
	print("Usage:netman.py -[als] argument")
	print("Examples:")
	print('netman -a "command:description"')
try:
	if sys.argv[1] == "-a": # Appending data 
		lst=sys.argv[2].split(":")	
		with open("cmd.json","r") as fd:
			data = fd.read()
			if data and data is not None:
				data = json.loads(data)
			else:
				data = []
			with open("cmd.json","w") as fdw:
					data.append(lst)
					fdw.write(json.dumps(data))
	elif sys.argv[1] == "-l": # Print all commands
		with open("cmd.json","r") as fd:
			data = fd.read()
			if data:
				for i in json.loads(data):
					print(f"{i[0]} : {i[1]}")
			else:
				print("No Info")
	elif sys.argv[1] == "-k": # Search for command
		with open("cmd.json","r") as fd:
			data = fd.read()
			if data:
				for i in json.loads(data):
					temp=list(filter(lambda x: x in i[1] , sys.argv[2].split(" ")))
					if temp:
						print(f"{i[0]} : {i[1]}")
					else:
						continue
	else:
		help_msg()
except:
	help_msg()
