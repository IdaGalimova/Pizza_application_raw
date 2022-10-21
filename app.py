from flask import Flask, render_template, request, redirect
import csv, random
from datetime import datetime
import os.path

app = Flask(__name__)

pepperoni_amount = 0

data = "NULL"
id = 0

raw_pepperoni_data, raw_hawaii_data = {}, {}
pepperoni_price = 10
hawaii_price = 15
raw_hawaii_data['hawaii_amount'] = 0

def calculate_price(pizza_amount, price):
    total = 0
    total = (pizza_amount*price)
    return total

def generate(id):
    Now = datetime.now()
    time = Now.strftime("%H:%M:%S")
    time = time.lstrip('0')
    time = time.lower()

    if id <= 999:
        id = id + 1
    else:
        id = 100
    return time, id


filename = "order_data.csv"

if os.path.exists(filename):
    os.remove(filename)


@app.route('/returnjson1', methods=['POST'])
def ReturnPepperoni():
    global raw_pepperoni_data
    
    raw_pepperoni_data = request.get_json()

    return "OK"

@app.route('/returnjson2', methods=['POST'])
def ReturnHawaii():
    global raw_hawaii_data
    
    raw_hawaii_data = request.get_json()

    return "OK"

@app.route("/table_number", methods=['POST'])
def get_table_number():
    global table_number
    table_number = request.form['table_number']

    return redirect('/confirmation_page')


@app.route("/")
def home_page():
    global raw_pepperoni_data, raw_hawaii_data
    raw_pepperoni_data, raw_hawaii_data = {}, {}

    return render_template("home.html", pepperoni_amount=pepperoni_amount)


@app.route("/shopping_cart")
def shopping_cart_page():
    global raw_order_data
    raw_order_data = raw_pepperoni_data | raw_hawaii_data

    print("Pepperoni data:", raw_pepperoni_data)
    if 'pepperoni_amount' in raw_pepperoni_data.keys():
        total_pepperoni_price = calculate_price(raw_pepperoni_data['pepperoni_amount'],10)
    else:
        total_pepperoni_price = 0
    if 'hawaii_amount' in raw_hawaii_data.keys():
        total_hawaii_price = calculate_price(raw_hawaii_data['hawaii_amount'],15)
    else:
        total_hawaii_price = 0

    total_price = total_pepperoni_price + total_hawaii_price


    return render_template("shopping_cart.html", raw_order_data=raw_order_data,total_pepperoni_price=total_pepperoni_price, total_hawaii_price=total_hawaii_price,total_price=total_price)

@app.route("/confirmation_page")
def confirmation_page():
    global id, general_data_list, order_list
    order = {}
    order_list = []

    time, id = generate(id)

    header = ['ID', "table_number", "time", "order"]

    data = {'ID': '0', "table_number": '0', "time": "0", "order": "0"}

    data["ID"] = id
    data["table_number"] = table_number
    data["time"] = time
    data["order"] = raw_order_data

    file_exists = os.path.isfile(filename)

    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        if not file_exists:
            writer.writeheader() 

        writer.writerow(data)

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        general_data_list = []
        for line in reader:
            general_data_list.append(line)
        # print("General data list:", general_data_list)

    for general_data in general_data_list:
        
        lcls = locals()
        exec("order = " + general_data["order"], globals(), lcls)
        order = lcls["order"]
        order_list.append(order)
        # print("ORDER LIST:", order_list)
    # print("Order list:", order_list)

    displayed_general_data = general_data_list[len(general_data_list) - 1]

    return render_template("confirmation.html", order=order, displayed_general_data=displayed_general_data)

@app.route("/luigi")
def luigiview():
    list_length = len(general_data_list)
    

    return render_template("luigiview.html", general_data_list=general_data_list, order_list=order_list, list_length = list_length)


if __name__ == '__main__':
    app.run()
