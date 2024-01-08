#!/usr/bin/python3
import sys
import netmiko
import re
from netmiko import ConnectHandler
from time import sleep


device = {
    'device_type': 'cisco_ios',
    'host': '{}'.format(sys.argv[1]),
    'username': 'nes470user',
    'password': 'nes470passwd',
}                                   # passing the parameters to login using a dictionary

router_conn = ConnectHandler(**device)


output1 = router_conn.send_command("show processes\n")   # Send the command and print the result
output2 = router_conn.send_command("show processes memory\n") #show you the output of the command


n = sys.argv[2]      # saving # of processes we want to show
n = int(n)      
pid_table = []  
Memory = []    
output1_lines = output1.split("\n") 
output2_lines = output2.split("\n") 
output2_lines = output2_lines[8:]  

for memory in output2_lines :       #This used to get the memory Allocated & saveing them in Dictionary
	mem = memory.split()	
	if len(mem) > 2 :
	   Memory.append({"memory":mem[2]})
	
numberOfP = len(output1_lines) - 2 #This will save number Of Processes we have & -2 to skip 1st & 2nd lines

if n > numberOfP :
	n = numberOfP
	
for line in output1_lines[2:] :          # We started from 2 to skip the 1st & 2nd lines/0 & 1(as index)
	 fields = line.split(maxsplit=7)  
	 				 # we used maxsplit=7 so it will not split the name/Try to print it
	 pid_table.append({              # here we saved them as a dictionary 
	 "PID":fields[0],
	 "name":fields[7],
	 "invoked":fields[4]})

	 
print("PID   P. Name           Mem. Allocated   No. Invoked")
print("---   -------------     --------------   -----------")

for i in range(n) :
	print('{:<4}'.format(pid_table[i]["PID"])," ", end='') 
	print('{:<13}'.format(pid_table[i]["name"])," ",end='')	
	print('{:<16}'.format(Memory[i]["memory"]),"",end='')
	print('{:<11}'.format(pid_table[i]["invoked"])," ",end='')
	print()
