from urllib.request import Request, urlopen


req = Request('http://danielbeumjoo.com', headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(req)
print(response.info())
print("-----------")
print(req.type)
print("-----------")
webpage = urlopen(req).read()
print(webpage[:150])
