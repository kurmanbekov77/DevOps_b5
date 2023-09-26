
# Company wants to increase their server according to their CPU usage. 
# Create a python program that gets average cpu usage as an input 
# and prints True if we need to launch more servers for our application.
# When average cpu usage is between 40 and 70 inclusive
# we should launch a new server.




cpu_usage = int(input("Enter average usage between 40 and 70 here:" )) 
more_server = int(input("Enter server quantity here:"))

server_for_applacation = cpu_usage > more_server
40< cpu_usage <70

print("We should launch new server" , server_for_applacation)
