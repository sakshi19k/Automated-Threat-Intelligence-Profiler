import requests
import json

# --- CONFIGURATION ---
# Replace 'YOUR_API_KEY_HERE' with your actual VirusTotal API key

VT_API_KEY = "32e5bc3ce300f8ef72c539ef4ba61a60ebffc1926c1a062f823ee42b5a52fb79"

def check_ip_virustotal(ip_address):
    """Queries the VirusTotal API for IP address reports."""
    print(f"[*] Querying VirusTotal for IP: {ip_address}...")
    
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
    headers = {
        "accept": "application/json",
        "x-apikey": VT_API_KEY
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Extract the analysis statistics (how many security vendors flagged it)
            stats = data['data']['attributes']['last_analysis_stats']
            
            print("\n--- THREAT INTELLIGENCE REPORT ---")
            print(f"Target IP: {ip_address}")
            print(f"Malicious Flags: {stats['malicious']}")
            print(f"Suspicious Flags: {stats['suspicious']}")
            print(f"Harmless Flags: {stats['harmless']}")
            print("----------------------------------\n")
            
            if stats['malicious'] > 0:
                print("[!] WARNING: This IP has been flagged as malicious!\n")
            else:
                print("[+] This IP appears clean based on current OSINT data.\n")
                
        else:
            print(f"[-] Error: Received status code {response.status_code} from VirusTotal.")
            
    except Exception as e:
        print(f"[-] An error occurred: {e}")

# --- EXECUTION ---
# Let's test it with Google's public DNS (should be clean)
check_ip_virustotal("8.8.8.8")

# Let's test it with a dummy malicious IP format to see how it handles it
# Replace this with a real malicious IP later when you research an APT!
check_ip_virustotal("31.220.104.32")