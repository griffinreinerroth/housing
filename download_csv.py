import csv
import requests
import pandas as pd
import io

url = 'https://files.zillowstatic.com/research/public_v2/zhvi/Neighborhood_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_mon.csv'

# Download Method 1: pandas read csv
data = pd.read_csv(url)


# Download Method 2: requests download csv

# what does requests.Session() do?
with requests.Session() as s:
    download = s.get(url)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)

