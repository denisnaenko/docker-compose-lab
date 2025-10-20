import time
import requests

time.sleep(3)

url = "http://server:8000/getfile"
try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        with open("received.txt", "wb") as f:
            f.write(response.content)
        print("File received successfully!\n")
        print(response.text)
    else:
        print("Failed to get file from server:", response.status_code)
except Exception as e:
    print("Error contacting server:", e)
