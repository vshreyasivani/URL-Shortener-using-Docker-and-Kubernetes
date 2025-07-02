import requests
import concurrent.futures
import time

URL = "http://localhost:8080/shorten"
payload = {"url": "https://en.wikipedia.org/wiki/Artificial_intelligence"}

def send_request():
    try:
        response = requests.post(URL, json=payload)
        print(response.status_code)
    except Exception as e:
        print("Error:", e)

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    while True:
        futures = [executor.submit(send_request) for _ in range(100)]
        concurrent.futures.wait(futures)
        time.sleep(0.1)
