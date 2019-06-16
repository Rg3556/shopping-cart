### SETUP
#
## shopping cart Repo Setup
#

# shopping_cart.py

# from pprint import pprint

import datetime


import csv
import sys
import pprint


csv_file_path = "Products Database.csv" # a relative filepath

with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    # reader = csv.reader(csv_file) # if your CSV doesn't have headers
    # for row in reader:
    #     print(row["id"], row["name"], row["department"], row["aisle"], row["price"])

    dict_list = []
    for line in reader:
        dict_list.append(line)
    # pprint.pprint(dict_list)



products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# print(products)
# pprint(products)


## Data Setup




### Basic Requirements

## Identifier / Input

subtotal_price = 0
selected_ids = []
valid_ids = [str(p["id"]) for p in dict_list] 


while True:
    selected_id = input("Please input a product identifier, or 'DONE': ") #> String input
    
    if selected_id == "DONE":
        break

    elif str(selected_id) in valid_ids: 
        # matching_products = [p for p in products if str(p["id"]) ==  str(selected_id)]
        # matching_product = matching_products[0]
        # total_price = total_price + matching_product["price"]
        # print("..." + matching_product["name"] + " " + str(matching_product["price"] ))
        selected_ids.append(selected_id)

    else:
        print("---------------------------------")
        print("OH, detected invalid input! Please try again...")
        print("---------------------------------")
        next # proceeds into the next iteration of the loop (OK to omit in this basic example because there is no more code following it inside the loop before the loop repeats)

## Receipt / Output

print("---------------------------------")
print("GREEN FOODS GROCERY")
print("WWW.GREEN-FOODS-GROCERY.COM")
print("---------------------------------")

today = datetime.date.today()
now = datetime.datetime.now()
print("CHECKOUT AT: " +  str(now.strftime("%Y-%m-%d ")) + str(now.strftime("%I:%M %p")))# + 2019-06-06 11:31 AM
print("---------------------------------")
print("SELECTED PRODUCTS: ")

# print(selected_ids)


for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    subtotal_price = subtotal_price + matching_product["price"]
    subtotal_usd = "${0:.2f}".format(subtotal_price)
    tax = subtotal_price* 0.0875
    tax_usd = "${0:.2f}".format(tax)
    total = subtotal_price + tax
    total_usd = "${0:.2f}".format(total)
    price_usd = "${0:.2f}".format(matching_product["price"])
    print("..." + matching_product["name"] + " "+ "("  + price_usd + ")")



print("---------------------------------")
print("SUBTOTAL: " + str(subtotal_usd))
print("TAX: " + str(tax_usd))
print("TOTAL: " + str(total_usd))  
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")





# A grocery store name of your choice
# A grocery store phone number and/or website URL and/or address of choice
# The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2019-06-06 11:31 AM)
# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $1.50)
# The total cost of all shopping cart items, formatted as US dollars and cents (e.g. $4.50), calculated as the sum of their prices
# The amount of tax owed (e.g. $0.39), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
# The total amount owed, formatted as US dollars and cents (e.g. $4.89), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
# A friendly message thanking the customer and/or encouraging the customer to shop again



## Writing Receipts to File 

file_name =  now.strftime("%Y-%m-%d-%I-%M-%S-%f") + ".txt" # a relative filepath

with open(file_name, "w") as file: # "w" means "open the file for writing"
    file.write("---------------------------------\n")
    file.write("GREEN FOODS GROCERY\n")
    file.write("WWW.GREEN-FOODS-GROCERY.COM\n")
    file.write("---------------------------------\n")
    file.write("CHECKOUT AT: " +  str(now.strftime("%Y-%m-%d ")) + str(now.strftime("%I:%M %p\n"))) # file.write 2019-06-06 11:31 AM
    file.write("---------------------------------\n")
    file.write("SELECTED PRODUCTS: \n")
    for selected_id in selected_ids:
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0]
        price_usd = "${0:.2f}".format(matching_product["price"])
        file.write("..." + matching_product["name"] + " "+ "("  + price_usd + ")")
        file.write("\n")
    file.write("---------------------------------\n")
    file.write("SUBTOTAL: " + str(subtotal_usd) + "\n")
    file.write("TAX: " + str(tax_usd) + "\n")
    file.write("TOTAL: " + str(total_usd) + "\n")  
    file.write("---------------------------------\n")
    file.write("THANKS, SEE YOU AGAIN SOON!\n")
    file.write("---------------------------------\n")
file_name = file_name + now.strftime("%Y-%m-%d-%I%M%S")


## Sending Receipts via Email

import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDGRID_TEMPLATE_ID = os.environ.get("SENDGRID_TEMPLATE_ID", "OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

#print("API KEY:", SENDGRID_API_KEY)
#print("TEMPLATE ID:", SENDGRID_TEMPLATE_ID)
#print("EMAIL ADDRESS:", MY_ADDRESS)



template_data = {
    "total_price_usd": str(total_usd),
    "human_friendly_timestamp": str(now.strftime("%Y-%m-%d ")) + str(now.strftime("%I:%M %p\n")),
    "products":[p for p in products if str(p["id"]) == str(selected_id)]
} # or construct this dictionary ["name"]ynamically based on the results of some other process :-D

client = SendGridAPIClient(SENDGRID_API_KEY)
print("CLIENT:", type(client))

message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS)
print("MESSAGE:", type(message))

message.template_id = SENDGRID_TEMPLATE_ID

message.dynamic_template_data = template_data

try:
    response = client.send(message)
    print("RESPONSE:", type(response))
    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as e:
    print("OOPS", e)