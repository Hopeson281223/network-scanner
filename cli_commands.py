import os #import OS module for system commands

def ping(host):
    """Pings a given host"""
    response = os.system(f"ping -n 4 {host}") #sending 4 pings
    return response == 0

def traceroute(host):
    """Runs traceroute to a given host."""
    os.system(f"tracert {host}") #running a traceroute command

if __name__ == "__main__":
    option = input("Enter command (ping / traceroute):").strip().lower()
    host = input("Enter target IP or domain: ")

    if option == "ping":
        if ping(host):
            print(f"{host} is reachable")
        else:
            print(f"{host} is unreachable")
    elif option == "traceroute":
        traceroute(host)
    else:
        print("Invalid command")