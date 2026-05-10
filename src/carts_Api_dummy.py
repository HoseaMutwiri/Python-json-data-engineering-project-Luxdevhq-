# libraries required

import json
import requests as re
import csv
from datetime import datetime


# define the url and the data file path

cart_data_url = "https://dummyjson.com/carts"

today = datetime.now().strftime("%Y%m%d_%H%M%S")

path = f"data\cart_data{today}.csv"

# API request
def send_request(url):
    data = re.get(url).json()
    return data


cart_data = send_request(cart_data_url)

print(json.dumps(cart_data,indent=2))
# extract wanted data values from the json file

list_data = []

for cart in cart_data["carts"]:
    cart_id = cart["id"]
    for product in cart["products"]:
        product_id = product["id"]
        product_name = product["title"]
        price = product["price"]
        quantity = product["quantity"]
        total = float(price)*int(quantity)
        list_data.append([cart_id,product_id,product_name,price,quantity,total])

# print(list_data)
# insert column names into the list_data
list_data.insert(0,["cart_id","product_id","product_name","price","quantity","total"])

# write the list_data into csv file 

with open(path,"w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(list_data)