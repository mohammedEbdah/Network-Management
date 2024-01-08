# Network-Management
Some Network Management codes with Descriptions for each code document
for the snmp connection code
To develop a simple network automation program utilizing the CLI.
In this code, we developed a Python script that acts as a minimalist network
automation application. The network management application implements a remote counterpart to the Linux’s top utility by sending the required commands to a Cisco router, and receiving and displaying their output in a convenient, well-formatted manner.
The script requirements are as follows:
1. The script accepts two command line arguments:
• The IP address of the router, e.g., 192.168.1.101
• An integer, n, representing the maximum number of processes to display their information.
For example, the script must be run as follows
python3 file_name 192.168.1.19 7
2. The script will be executed on a Linux machine.
3. The script sends the appropriate command(s) to the router to obtain the list of processes
and their information.
4. The script displays on the standard output the following information for each of the
n processes: the process ID (PID), the process name, the memory allocated by the
virtual process, and the number of times the process has been invoked.
5. we will make the output in the following format
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
6. The processes in the output must be ordered based on the PID and in ascending order.




7. The script uses the netmiko package to be able to talk to the Cisco router.
