import requests

#print(requests.__version__)
#response = requests.get("http://google.com/")
response = requests.get("https://raw.githubusercontent.com/sruduke/cmput404-lab1/master/lab1.py")
print(response.text)
