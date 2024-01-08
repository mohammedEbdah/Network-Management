the full decription for the mib document code 
for the mib document code
To develop a network management application utilizing the SNMP operations provided via
the Easy SNMP Python APIs.
In this module, we will develop a Python script that acts as a minimalist network
management application. The network management application interrogates the SNMP
agent for the information about a list of processes and displays it in a convenient, wellformatted manner.
  The script requirements are as follows:
The script accepts the following three command line arguments
• The read-only community string of the agent, e.g., public.
• The IP address of the CSR1000v router where the agent is running, e.g., 192.168.1.101.
• An integer, n, representing the maximum number of processes to display their
information.
For example, the script will be run as follows
python3 ./xxxxxx.py public 192.168.1.101 7
where ‘xxxxxx’ is your file name.
The script will be executed on a Linux machine.
The script sends appropriate SNMP requests to the SNMP agent, and retrieves the
information about the processes running on the CSR1000v router.
The script displays on the standard output the following information for each of the
n processes: the process ID (PID), the process name, the memory allocated by the
virtual process, and the number of times the process has been invoked.
The output will be in the following format
PID P. Name Mem. Allocated No. Invoked
--- ------------- -------------- -----------
1 Chunk Manager 1297032 26
2 Load Meter 448 1781
3 MCP TIPC 0 61
...
...
...
...
7 EDDRI MAIN 65632 1
The processes in the output will be ordered based on the PID and in ascending order.
