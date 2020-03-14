# post with requests

import requests
import json

# json standar library allows:
# .dumps() --> string that is json
# .dump() --> ouotputs a text file that is json

filipe = {
    'name': 'FILIPE PV',
    'SuperPower': 'Patience...',
    'prep level': 'wine and batteries for the xbox'
}

#json.dump(filipe, 'filie_json')

# a post needs:
# header and url
# json object

json_body_body = json.dumps({
"postcodes": ["e147le", "SE172HY", "ne30 1dp", "N182AA"]
})

header = {'Content-type': 'application/json'}

url = "http://api.postcodes.io/postcodes/"

# Making POST api call with json_body, header and url
resq = requests.post(url, headers = header, data = json_body_body)

## working the request is exactly the same thing

response_json = resq.json()