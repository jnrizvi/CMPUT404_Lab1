import requests

print(requests.__version__)
homePageUrl = "http://www.google.com/"

response = requests.get(homePageUrl)

# reference: http://zetcode.com/python/requests/
print(response.text)

rawGHURL = "https://raw.githubusercontent.com/jnrizvi/CMPUT404_Lab1/main/script.py"
response = requests.get(rawGHURL)

print(response.text)