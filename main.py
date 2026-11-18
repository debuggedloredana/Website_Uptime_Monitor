import requests
import json
import os
from datetime import datetime


websites = [
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.example.com",
    "https://this-website-does-not-exist-12345.com"
]

if os.path.exists("history.json"):
    with open("history.json", "r") as file:
        history = json.load(file)
else:
    history = []

response_times = []
successful_websites = 0

for website in websites:
    try:
        response = requests.get(website, timeout=5)
    except requests.exceptions.ConnectionError:
        print(website, "Connection failed.")
        save_record = {
            "website": website,
            "status": "Connection failed.",
            "timestamp": datetime.now().isoformat(timespec="seconds")
                }
        history.append(save_record)
        continue
    except requests.exceptions.Timeout:
        print(website, "Timed out.")
        save_record = {
            "website": website,
            "status": "Timeout.",
            "timestamp": datetime.now().isoformat(timespec="seconds")
        }
        history.append(save_record)
        continue
    response_time_ms = response.elapsed.total_seconds() * 1000
    response_times.append(response_time_ms)
    
    average = round(sum(response_times)/ len(response_times),2)

    check_record = {
    "website": response.url,
    "status_code": response.status_code,
    "response_time_ms": round(response_time_ms, 2),
    "status": "Online" if response.status_code == 200 else "Error",
    "timestamp": datetime.now().isoformat(timespec="seconds")  
    }
    history.append(check_record)
    
    if response.status_code == 200:
        print(response.url, "Online", round(response_time_ms, 2), "ms")
        successful_websites = successful_websites + 1
    else:
        print(response.url, "Error", round(response_time_ms, 2), "ms")   
    if response_time_ms < 500:
        print("Fast response")
    else:
        print("Slow response")

average = round(sum(response_times)/ len(response_times),2)
success_rate = round(successful_websites/ len(websites) *100 ,2) 


with open("history.json", "w") as file:
    json.dump(history, file, indent=4)

print("-------------------------------")
print("OVERALL MONITORING STATISTICS")
print("-------------------------------")
print("Total websites monitored:" ,len(websites))
print("Successful responses:", successful_websites)
print("Success rate:", success_rate)
print("Average response time:", average, "ms")


