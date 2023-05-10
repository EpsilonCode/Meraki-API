import requests

# Meraki API key and organization ID
MERAKI_API_KEY = "Your Meraki API Key"
ORGANIZATION_ID = "Your Meraki Org ID"

# API endpoint to get networks for an organization
NETWORKS_ENDPOINT = f"https://api.meraki.com/api/v0/organizations/{ORGANIZATION_ID}/networks"

# Make API request to get networks
headers = {
    "X-Cisco-Meraki-API-Key": MERAKI_API_KEY,
    "Content-Type": "application/json"
}
response = requests.get(NETWORKS_ENDPOINT, headers=headers)

# Check for errors and parse response
if response.status_code != 200:
    print("Error retrieving networks:", response.text)
else:
    networks = response.json()

    # Print network names and IDs
    for network in networks:
        print("{} ({})".format(network["name"], network["id"]))
