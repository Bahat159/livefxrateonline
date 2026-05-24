import json
import urllib.request
import urllib.parse

def fetch_and_send_rates():
    # A reliable public API to get real-time currency rates
    website_url = "https://er-api.com"
    url = "https://v6.exchangerate-api.com/v6/b2039c00936e994b7e58c2e3/latest/USD"
    
    try:
        # 1. Fetch the live exchange data
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())

                #print(f"{data}")
                
                # Extract USD to NGN (Nigerian Naira) rate
                ngn_rate = data["conversion_rates"].get("NGN", 0)
                timestamp = data.get("time_last_update_utc", "Unknown")
                
                print(f"Success: Live Rate found - 1 USD = {ngn_rate} NGN")
                
                # 2. Prepare data payload to send to your PHP backend
                payload = {
                    "currency": "NGN",
                    "rate": ngn_rate,
                    "updated_at": timestamp
                }
                
                # 3. Send the data to your PHP script via a POST request
                # Replace with your actual live server URL when deployed
                backend_url = "http://localhost:80/livefxrateonline/backend/process_data.php" 
                
                encoded_data = urllib.parse.urlencode(payload).encode('utf-8')

                req = urllib.request.Request(backend_url, data=encoded_data, method="POST")

                try:
                    with urllib.request.urlopen(req) as backend_response:
                        print("\nBackend Response:", backend_response.read().decode('utf-8'))
                except urllib.error.HTTPError as e:
                    # 4. Print the error body for debugging
                    print(f"HTTP Error: {e.code} - {e.read().decode('utf-8')}")
                except urllib.error.URLError as e:
                    print(f"URL Error: {e.reason}")

                
                
            else:
                print("Error: Could not fetch data from the API.")
                
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    fetch_and_send_rates()
