import requests
import time

# Meraki API key and network ID
MERAKI_API_KEY = "Your Meraki API Key"
NETWORK_ID = "Your Meraki Network ID"

# API endpoint to get clients for a network
CLIENTS_ENDPOINT = "https://api.meraki.com/api/v0/networks/{}/clients".format(NETWORK_ID)

# Function to get new clients on the network
def get_new_clients():
    # Make API request to get clients
    headers = {
        "X-Cisco-Meraki-API-Key": MERAKI_API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.get(CLIENTS_ENDPOINT, headers=headers)

    # Check for errors and parse response
    if response.status_code != 200:
        print("Error retrieving clients:", response.text)
        return []
    else:
        clients = response.json()

    # Filter out clients that have been seen before
    new_clients = []
    for client in clients:
        if client.get("status") == "Online":
            if "dhcpHostname" in client and client["dhcpHostname"] not in seen_clients:
                new_clients.append(client)
                seen_clients.add(client["dhcpHostname"])
            elif "ip" in client and client["ip"] not in seen_clients:
                new_clients.append(client)
                seen_clients.add(client["ip"])

    # Print new clients
    if new_clients:
        print("New clients:")
        for client in new_clients:
            if "dhcpHostname" in client:
                print("- {} ({})".format(client["description"], client["dhcpHostname"]))
            elif "ip" in client:
                print("- {} ({})".format(client["description"], client["ip"]))

# Set up a set to keep track of seen clients
seen_clients = set()

# Continuously check for new clients every two hours
while True:
    get_new_clients()
    time.sleep(7200)  # Sleep for two hours
