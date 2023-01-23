# Wifi Scanner
The script is a Python script that checks if the WiFi drivers are installed on an Ubuntu system, if not it installs them and loads them, then it scans for nearby WiFi networks, saves the detailed results of open networks in a file, sorts the networks by signal strength and connects to them one by one, staying connected for 10 minutes before moving to the next network.

# Run the script
Ensure that you have Python 3 installed on your system. You can check the version of Python by running the command python3 --version in the terminal.

You will need to install the tqdm library, which is used to display the progress bar while scanning for WiFi networks. You can install it by running the command pip3 install tqdm in the terminal. 

Next, create a new file on your system, and copy the script provided above into it. Save the file with a .py extension, for example, wifi_script.py

Make the script executable by running the command chmod +x wifi_script.py in the terminal.

To run the script, open a terminal and navigate to the directory where the script is saved. Then run the command ./wifi_script.py
