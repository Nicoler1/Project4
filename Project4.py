import nmap
import datetime

#Time & date report was ran.
current_datetime = datetime.datetime.now()
format_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

#Text displaying beside the timestamp.
print(f'Script execution timestamp: {format_datetime}')

#The class used from the python-nmap library.
Port_Scanner = nmap.PortScanner()

#Host we are scanning with port range.
Target_Host = '127.0.0.1'
Common_ports = [80, 443, 20, 21]

#Text displaying beside the host.
print(f'Host Scanned: {Target_Host}')

#Scanner Parameters
for port in Common_ports:
    output = Port_Scanner.scan(Target_Host, str(port))
    port_state = output['scan'][Target_Host]['tcp'][port]['state']
    service = output['scan'][Target_Host]['tcp'][port]['name']
    
    print(f'Port {port} is {port_state} ({service}). ')

