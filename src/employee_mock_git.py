# github url difined
employee_gitmock_url = "https://raw.githubusercontent.com/HoseaMutwiri/Python-json-data-engineering-project-Luxdevhq-/main/employee_raw_data_mock.json"

# import neccessary libraries

import pandas as pd
import requests as re
from datetime import datetime
import json
import csv

# send request and get data function

def send_request(url):
    data = re.get(url).json()
    return data


# confrim the request as successful

try:
    mock_raw = send_request(employee_gitmock_url)
    print("request successful")
except re.exceptions.RequestException as error:
    print(f"request unsuccessful {error}")
    


# convert the data to a data frame

employee_mock_df = pd.DataFrame(mock_raw)

# print the first 2 rows of employee_mock_df

print(employee_mock_df.head(2))

# generate today data
today = datetime.now().strftime("%Y%m%d")

# define the path to write the csv file

data_csv_folder = f"data/mock_employee_data{today}.csv"

# write the dataframe to csv formart

employee_mock_df.to_csv(data_csv_folder,index=False)

