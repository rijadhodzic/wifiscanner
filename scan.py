import os
import time
from tqdm import tqdm

def check_wifi_drivers():
    # check if wifi drivers are installed
    drivers_installed = os.system("lsmod | grep -i 'rtl8723be'")
    if drivers_installed != 0:
        # install wifi drivers
        os.system("sudo apt-get update")
        os.system("sudo apt-get install rtl8723be-dkms")
        os.system("sudo modprobe rtl8723be")
    else:
        print("WiFi drivers are already installed.")

def scan_wifi():
    # scan for wifi networks
    print("Scanning for WiFi networks...")
    os.system("sudo iwlist wlan0 scan | grep ESSID > wifi_scan.txt")
    # filter for open networks
    os.system("grep 'ESSID:\"\"' wifi_scan.txt > open_wifi.txt")
    print("WiFi scan complete, detailed results of open networks saved in 'open_wifi.txt'")

def connect_wifi():
    if not os.path.exists("open_wifi.txt"):
        print("Error: open_wifi.txt not found. Make sure to run scan_wifi() first.")
        return
    # sort the networks by signal strength
    os.system("sort -k 6 -n open_wifi.txt > sorted_wifi.txt")
    # read the sorted list of networks
    with open("sorted_wifi.txt", "r") as f:
        wifi_list = f.readlines()
    if not wifi_list:
        print("Error: no open networks found.")
        return
    # connect to each network in order
    for wifi in wifi_list:
        ssid = wifi.split(":")[1].strip()
        os.system(f"sudo nmcli device wifi connect {ssid} ifname wlan0")
        print(f"Connected to {ssid}")
        time.sleep(600) # wait for 10 minutes

def main():
    check_wifi_drivers()
    with tqdm(total=100) as pbar:
        for i in range(100):
            time.sleep(0.05)
            pbar.update(1)
            if i == 99:
                scan_wifi()
    connect_wifi()

if __name__ == "__main__":
    main()
