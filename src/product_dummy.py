# libraries required

import json
import requests as re
import csv
from datetime import datetime
import pandas as pd


# define the url and the data file path

products_url = "https://dummyjson.com/products"

# function to send the request

def get_data(url):
    data = re.get(url).json()
    return data

try:
    product_dummy = get_data(products_url)
    print("request successful")
except re.exceptions.RequestException as error:
    print(f"request failed {error}")


print(product_dummy.keys())


product_norm_df = pd.json_normalize(product_dummy["products"])

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

print(timestamp)

products_df = pd.DataFrame(product_norm_df)

print(products_df.head(3))

print(products_df.columns)

subset_product_data = products_df[['id', 'title', 'description', 'category', 'price', 'discountPercentage',
       'rating', 'stock', 'brand', 'sku', 'weight',
       'warrantyInformation', 'shippingInformation', 'availabilityStatus']]

productspath = f"data/products_data{timestamp}.csv"

subset_product_data.to_csv(productspath,index=False)








