# CMPUT 404 Virtualenv & cURL Lab
# Sophia Ruduke

import requests

div = "-"*20 + "\n"

# virtualenv - 3
print("Requests Version", requests.__version__, div, sep="\n")

# curl - 5
response = requests.get("http://google.com/")
print("Google Request", response.text, div, sep="\n")

# curl - 10
response = requests.get("https://raw.githubusercontent.com/sruduke/cmput404-lab1/master/lab1.py")
print("Source Code", response.text, div, sep="\n")
