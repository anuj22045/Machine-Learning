import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/Mobile_country_code"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
}

response = requests.get(url, headers=headers)

tables = pd.read_html(response.text)

print(tables[0])
