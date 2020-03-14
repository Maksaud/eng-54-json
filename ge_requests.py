import requests


# GET request
# URL = path + arguments
# possibly headers and meta data
# postcode.io --> follow their documentation

# capture the input --> decrypt JSON to dictionary

# Get some data out

# Variables for GET request:
path = "http://api.postcodes.io/postcodes/"
argument = 'SE172HY'
url = path + argument

# make the API CALL
resq = requests.get(url)

print(resq)
print(resq.status_code)
print(resq.headers)
print(resq.content)

#nJSON decoder
print(resq.json())

dict_post_code = resq.json()
print(dict_post_code.keys())
print(type(dict_post_code))

## I want
# european_electoral_region
print(dict_post_code['result']['european_electoral_region'])
# outcode
print(dict_post_code['result']['outcode'])
# long
print(dict_post_code['result']['longitude'])
# lat
print(dict_post_code['result']['latitude'])