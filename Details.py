import psutil
import speedtest
import platform
import socket
import subprocess
import re
import wmi

# Function to get all installed software list
def get_installed_software():
    try:
        installed_software = subprocess.check_output('wmic product get name', shell=True, encoding='utf-16le').strip().split('\n')[1:]
        return installed_software
    except Exception as e:
        print(f"Error retrieving installed software: {e}")
        return []

# Function to get internet speed
def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # convert to Mbps
    upload_speed = st.upload() / 10**6  # convert to Mbps
    return download_speed, upload_speed

# Function to get screen resolution
def get_screen_resolution():
    return subprocess.check_output('wmic desktopmonitor get screenheight, screenwidth').decode('utf-8').strip().split('\n')[1]

# Function to get CPU details
def get_cpu_info():
    cpu_info = {}
    cpu_info['model'] = platform.processor()
    cpu_info['cores'] = psutil.cpu_count(logical=False)
    cpu_info['threads'] = psutil.cpu_count(logical=True)
    return cpu_info

# Function to get GPU model
def get_gpu_info():
    try:
        w = wmi.WMI()
        gpu_info = w.Win32_VideoController()[0].Name
        return gpu_info
    except Exception as e:
        return "No GPU detected"

# Function to get RAM size
def get_ram_size():
    ram = psutil.virtual_memory().total / (1024**3)  # Convert bytes to GB
    return ram

# Function to get screen size
def get_screen_size():
    # Provide your screen size calculation logic here
    return "Screen size information not available"

# Function to get MAC address
def get_mac_address():
    try:
        mac_addresses = psutil.net_if_addrs()
        wifi_mac = mac_addresses.get('Wi-Fi', [{'address': 'N/A'}])[0].address
        ethernet_mac = mac_addresses.get('Ethernet', [{'address': 'N/A'}])[0].address
        return wifi_mac, ethernet_mac
    except Exception as e:
        print(f"Error retrieving MAC address: {e}")
        return 'N/A', 'N/A'
    
# Function to get public IP address
def get_public_ip():
    return socket.gethostbyname(socket.gethostname())

# Function to get Windows version
def get_windows_version():
    return platform.version()


installed_software = get_installed_software()
download_speed, upload_speed = get_internet_speed()
screen_resolution = get_screen_resolution()
cpu_info = get_cpu_info()
gpu_info = get_gpu_info()
ram_size = get_ram_size()
screen_size = get_screen_size()
wifi_mac, ethernet_mac = get_mac_address()
public_ip = get_public_ip()
windows_version = get_windows_version()

print("Installed Software:", installed_software)
print("Internet Speed (Download, Upload) in Mbps:", download_speed, upload_speed)
print("Screen Resolution:", screen_resolution)
print("CPU Model:", cpu_info['model'])
print("Number of Cores:", cpu_info['cores'])
print("Number of Threads:", cpu_info['threads'])
print("GPU Model:", gpu_info)
print("RAM Size (GB):", ram_size)
print("Screen Size:", screen_size)
print("Wi-Fi MAC Address:", wifi_mac)
print("Ethernet MAC Address:", ethernet_mac)
print("Public IP Address:", public_ip)
print("Windows Version:", windows_version)
