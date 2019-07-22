import urllib.request, json

# Opening a web request
url = urllib.request.urlopen("https://{"query":{"count":1},"results":{"USD_PHP":{"id":"USD_PHP","val":51.335026,"to":"PHP","fr":"USD"}")
# Decoding response to str
data = json.loads(url.read().decode()) # Decoding a web request

# Parsing results
results = data['results']
USD_ILS = results['USD_ILS']
val = USD_ILS['val']
print(val)




