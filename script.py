import requests

print(requests.__version__)
homePageUrl = "http://www.google.com/"

response = requests.get(homePageUrl)

# reference: http://zetcode.com/python/requests/
print(response.text)