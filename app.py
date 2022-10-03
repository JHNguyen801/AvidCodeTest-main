import requests
import json
from pandas.io.json import json_normalize
import pandas as pd

api_url = 'https://mko2aswez1.execute-api.us-west-2.amazonaws.com/V1/AvidCodeTest'
headers = {'x-api-key': 'qaEMpgfPNC4wvRuApSEiD7HzNRGrKTkd1yBFiwXP',
           'Accept': 'application/json'
           }

# fetch API
response = requests.request("POST", api_url, headers=headers, data={})
data = response.text  # convert into text format

json_data = json.loads(data)  # parse data into dic
# data_json = response.json()

print("Checking the response code: ", response.status_code)
# print("Display JSON info: \n", response.text)  # display the JSON info

# write fetch api to JSON file
# file = open('test.json', 'w')
# file.write(data)

#
readfile = pd.read_json('test.json', orient='index')
csvdata = readfile.to_csv()

# print(csvdata)

# open json file and parse it
with open('test.json') as f:
    data = json.load(f)

df = pd.json_normalize(data)
print(df)

df.to_csv('hoang_customerloan.csv', index=True) # write dataframe file to csv


# use dataframe to export csv
# df = pd.DataFrame(data_json)
# df.to_csv('hoang_customerloan.csv')

