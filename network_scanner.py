from scapy.all import ARP, Ether, srp #Scapy modules for sending arp requests
import json #json module to save results
import csv #csv module to save results

def scan_network(network):
    """Scans the network for active devices using arp requests"""
    arp_request = ARP(pdst=network) #create arp request with the target protocol destination
    ether = Ether(dst="ff:ff:ff:ff:ff:ff") #create ethernet frame for broadcast
    packet = ether / arp_request #combine ethernet and arp requests

    answered_list, _ = srp(packet, timeout=2, verbose=False) #sending packets and receiving responses, _ is unansered requests which are ignored
    devices = [] #list to store ip and mac addreess of detected devices

    for sent, received in answered_list:
        devices.append({"IP": received.psrc, "MAC": received.hwsrc}) #append dictionary with src ip and mac to devices list

    return devices

def save_to_csv(devices, filename="output/scan_results.csv"):
    """Saves scan results to a csv file"""
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["IP","MAC"]) #creating csv writer
        writer.writeheader() #write header
        writer.writerows(devices) #write data

def save_to_json(devices, filename="output/scan_results.json"):
    """Saves scan results to a json file"""
    with open(filename, "w") as file:
        json.dump(devices, file, indent=4) #writing JSON data - converts devices list to json format and writes to file 4-space indentation for readability

"""Main execution block"""
if __name__ == "__main__":
    network = input("Enter the network to scan, eg, 192.168.1.0/24): ")
    results = scan_network(network)
    print("Devices found:", results)
    save_to_csv(results)
    save_to_json(results)
    print("Results saved to scan_results.csv and scan_results.json")
    
