from tqdm import tqdm
import subprocess
import stem.process
import time

def wifi_scan():
    print("Starting Tor process...")
    # Start the Tor process
    with stem.process.launch_tor_with_config(config={'SocksPort': "9050"}) as tor:
        # Wait for the Tor process to establish a connection
        for _ in tqdm(range(30), desc="Waiting for Tor connection"):
            if tor.is_alive():
                break
            time.sleep(1)
        print("Connected to Tor network.")
        # Update the SOCKS proxy settings to use the Tor socks port
        os.environ["all_proxy"] = "socks5h://127.0.0.1:9050"

        # Check the status of the Wi-Fi interface
        interface = "wlan0" # change this to the name of your interface
        output = subprocess.check_output(['ip', 'link', 'show', interface])
        output = output.decode()
        if "DOWN" in output:
            # Bring the interface up if it's down
            subprocess.run(['ip', 'link', 'set', interface, 'up'])
        # Run the command 'iwlist scan' to scan for nearby Wi-Fi networks
        output = subprocess.check_output(['iwlist', 'scan'])
        output = output.decode()

        # Split the output into a list of strings, one for each Wi-Fi network
        networks = output.split('Cell')[1:]

        # Open the file to save the information
        with open('wifi_networks.txt', 'w') as f:
            for network in networks:
                # Split the network information into a list of strings
                network_info = network.split('\n')

                # Get the network's ESSID (name)
                essid = network_info[0].split('ESSID:')[1].strip()

                # Check if the network is open or secured
                security = None
                for line in network_info:
                    if 'Encryption key:' in line:
                        security = line.split(':')[1].strip()
                        break
                if security == 'off':
                    security = 'Open'
                else:
                    security = 'Secured'

                # Write the network information to the file
                f.write(f'ESSID: {essid}, Security: {security}\n')

wifi_scan()