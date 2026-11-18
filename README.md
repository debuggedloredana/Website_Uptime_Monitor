Website Uptime Monitor

A Python-based website monitoring tool that checks website availability, measures response times and records monitoring results using JSON.

Project Overview

This project was developed to improve my Python programming skills and explore concepts related to website monitoring, networking and infrastructure.

The program monitors multiple websites, checks their HTTP status codes, measures their response times and stores monitoring results in a JSON history file.

Features

Website Monitoring: Checks multiple websites using HTTP requests.

HTTP Status Codes: Identifies successful responses and HTTP errors.

Response Time Tracking: Measures website response times in milliseconds.

Performance Classification: Classifies responses as fast or slow using a 500 ms threshold.

Error Handling: Handles connection failures and request timeouts without stopping the monitoring process.

JSON Storage: Saves monitoring results, including timestamps, in a JSON file.

Monitoring Statistics: Calculates the average response time and overall success rate.

Technologies Used

Python

Requests library

JSON

Git and GitHub

How to Run

Make sure Python is installed.

Clone or download this repository.

Install the required library:

pip install requests

Run the program:

python main.py

Project Structure

Website_Uptime_Monitor/
│
├── main.py
├── history.json
└── README.md

What I Learned

Through this project, I developed my understanding of:

Python loops, lists and dictionaries.

HTTP requests and status codes.

Measuring response times.

Exception handling using try and except.

Reading and writing JSON files.

Using Git and GitHub for version control and project management.

Future Improvements

Add a graphical interface to display monitoring results.

Introduce historical performance comparisons.

Expand monitoring statistics and reporting features.

This project was created as part of my independent Python learning and development.
