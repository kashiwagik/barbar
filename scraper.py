import urllib3
import requests
import csv
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.qbhouse.co.jp/search/668"

# pem="GlobalSign-GCC-R3.pem"
# context = ssl.create_default_context(cafile=certifi.where())
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
res = requests.get(url, verify=False)
soup = BeautifulSoup(res.text, 'html.parser')

el = soup.select_one("#salon_info > div > div.waiting > div.waiting_wrap > dl.number > dd > span")  # IDなどを指定して値を取得
if el:
    value = el.text
    if value and value.isdigit():
        with open("data.csv", "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().isoformat(), value])

