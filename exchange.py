import requests
import pandas as pd
import json

base_url = "https://api.apilayer.com/exchangerates_data/latest?BASE=BRL"
headers = {
    "apikey": "DnFoZdOtVd1durS3D6T8uSUFij76J7RF"
}

try:
    response = requests.get(base_url, headers=headers)
    response_json = response.json()
    # data = json.loads(response_json)
    dataframe = pd.json_normalize(response_json)
    print(dataframe)
except requests.exceptions.HTTPError as errh:
    print("Error: ", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error: ", errc)
except requests.exceptions.Timeout as errt:
    print("Error: ", errt)
except requests.exceptions.RequestException as err:
    print("Error: ", err)