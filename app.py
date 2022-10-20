from flask import Flask, render_template, request, redirect
import csv, random
from datetime import datetime
import os.path

app = Flask(__name__)

pepperoni_amount = 0

data = "NULL"
id = 0
raw_order_data = {}
@app.route('/returnjson1', methods=['POST'])
def ReturnJSON():
    global raw_order_data, pepperoni_amount
    raw_order_data = request.get_json()
    # raw_order_data["hawaii"] = request.get_json()

    return "OK"

@app.route("/table_number", methods=['POST'])
def get_table_number():
    global table_number
    table_number = request.form['table_number']

    return redirect('/confirmation_page')


@app.route("/")
def home_page():

    return render_template("home.html", pepperoni_amount=pepperoni_amount)


@app.route("/shopping_cart")
def shopping_cart_page():

    return render_template("shopping_cart.html", raw_order_data=raw_order_data)


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


@app.route("/confirmation_page")
def confirmation_page():
    global id, general_data_list, order
    print(table_number)

    time, id = generate(id)

    header = ['ID', "table_number", "time", "order"]

    data = {'ID': '0', "table_number": '0', "time": "0", "order": "0"}

    data["ID"] = id
    data["table_number"] = table_number
    data["time"] = time
    data["order"] = raw_order_data

    filename = "order_data.csv"
    file_exists = os.path.isfile(filename)

    # if os.path.exists(filename):
    #     os.remove(filename)
    

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

    for general_data in general_data_list:
        order = {}

        lcls = locals()
        exec("order = " + general_data["order"], globals(), lcls)
        order = lcls["order"]

    displayed_general_data = general_data_list[len(general_data_list) - 1]

    return render_template("confirmation.html", order=order, displayed_general_data=displayed_general_data)

@app.route("/luigi")
def luigiview():

     return render_template("luigiview.html", general_data_list=general_data_list, order=order)


if __name__ == '__main__':
    app.run()
