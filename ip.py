import requests
import chardet

response  = requests.get("https://link.dns.pub/a53fae17100001026365/b06df6f618")

print(response.text)