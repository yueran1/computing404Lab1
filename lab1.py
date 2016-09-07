import requests

response2= requests.get('http://google.ca')
response =requests.post('http://ccid-eddieantonio.rhcloud.com/yueran1')
print response.status_code

print requests.__version__