#Saif Bakhet 140552
#Mohammed Ibdah 142639
#! /usr/bin/python3

import sys

from easysnmp import Session

s = Session(hostname = sys.argv[2] , community = sys.argv[1] , version = 2 , use_numeric = True, use_sprint_value = True )

n = int(sys.argv[3])

print("PID   P. Name           Mem. Allocated   No. Invoked")

print("---   -------------     --------------   -----------") 



r = s.get_next('.1.3.6.1.4.1.9.9.109.1.4.1.1.1.7.20755')



name=[]

pid=[]

allocate=[]

invok=[]

newoid = str(r.oid)+'.'+str(r.oid_index)

SP2 = newoid.split('.')



while SP2[14] == '2': 

	r = s.get(newoid)

	sname=r.value.strip('"')

	sname=sname[:16]

	name.append(sname)

	pid.append(r.oid_index)

	r = s.get_next(newoid)	

	newoid = str(r.oid)+'.'+str(r.oid_index)	

	SP2 = newoid.split('.')

	

locate_oid = '.1.3.6.1.4.1.9.9.109.1.4.1.1.6.7.20755'

r = s.get_next(locate_oid)

newoid = str(r.oid)+'.'+str(r.oid_index)	

SP6 = newoid.split('.')



while SP6[14] == '6':

	r = s.get(newoid)

	allocate.append(r.value)

	r = s.get_next(newoid)

	newoid = str(r.oid)+'.'+str(r.oid_index)	

	SP6 = newoid.split('.')

	

IN_oid = '.1.3.6.1.4.1.9.9.109.1.4.1.1.8.7.20755'

r = s.get_next(IN_oid)

newoid = str(r.oid)+'.'+str(r.oid_index)	

SP8 = newoid.split('.')



while SP8[14] == '8':

	r = s.get(newoid)	

	invok.append(r.value)

	r = s.get_next(newoid)

	newoid = str(r.oid)+'.'+str(r.oid_index)

	SP8 = newoid.split('.')



size = len(pid)

if n > size :

	n = size

z = 0

while (z < n):

	print('{:6}{:18}{:17}{:11}'.format(pid[z],name[z],allocate[z],invok[z]))

	z = z + 1

	

	

		

	

	

