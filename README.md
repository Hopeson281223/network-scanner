# Network Scanner

## Description

The **Network Scanner** is a Python-based tool designed to scan local networks and identify active devices. It provides details such as IP addresses and MAC addresses of connected devices, helping users analyze their network security.

## Features

- Scans the local network for connected devices.
- Displays IP and MAC addresses of detected devices.
- Uses ARP requests to identify active hosts.
- Lightweight and fast.

## Requirements

Make sure you have the following dependencies installed:

```bash
pip install scapy
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Hopeson281223/network-scanner.git
   ```
2. Navigate to the project directory:
   ```bash
   cd network-scanner
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with administrator privileges:

```bash
python scanner.py -t 192.168.1.1/24
```

Replace `192.168.1.1/24` with your target subnet.

## Example Output

```
IP Address       MAC Address
-----------------------------------
192.168.1.2      AA:BB:CC:DD:EE:FF
192.168.1.3      11:22:33:44:55:66
```

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author

[Hopeson281223](https://github.com/Hopeson281223)
