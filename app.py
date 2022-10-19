from flask import Flask, render_template, request, jsonify
import csv, random
from datetime import datetime


app = Flask(__name__)

pepperoni_amount = 0

data = "NULL"
id = 0

@app.route('/returnjson1', methods=['POST'])
def ReturnJSON():
    global raw_order_data, pepperoni_amount
    raw_order_data = request.get_json()

    return "OK"


@app.route("/")
def home_page():

    return render_template("home.html", pepperoni_amount=pepperoni_amount)


@app.route("/shopping_cart")
def shopping_cart_page():
    # for key, value in order_info.items():
    #     print(key, value)
    # if order_info =

    return render_template("shopping_cart.html", raw_order_data=raw_order_data)


def generate(id):
    
    table = random.randint(0, 5)
    # EstTime = "15 minutes"
    Now = datetime.now()
    time = Now.strftime("%H:%M:%S")
    time = time.lstrip('0')
    time = time.lower()

    if id <= 999:
        id = id + 1
    else:
        id = 100
    print(time)
    print(id)
    return table, time, id


@app.route("/confirmation_page")
def confirmation_page():
    
    table, time, id1 = generate(id)
    print(id1)


    header = ['ID', "table_number", "time", "order"]

    data = {'ID': '0', "table_number": '0', "time": "0", "order": "0"}

    data["ID"] = id1
    data["table_number"] = table
    data["time"] = time
    data["order"] = raw_order_data

    csv_file = "order_data.csv"

    # print(type(raw_order_data))

    with open(csv_file, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        # writer.writeheader()

        writer.writerow(data)

    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        general_data_list = []
        for line in reader:
            general_data_list.append(line)

    for general_data in general_data_list:
        order = {}

        lcls = locals()
        exec("order = " + general_data["order"], globals(), lcls)
        order = lcls["order"]
        print(order)

    displayed_general_data = general_data_list[len(general_data_list) - 1]

    return render_template("confirmation.html", order=order, displayed_general_data=displayed_general_data)


if __name__ == '__main__':
    app.run()
