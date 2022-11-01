from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime
import os.path

app = Flask(__name__)

id = 0
total_price = 0
total = 0 

prosciutto_crudo_price = 12.99
pepperoni_price = 9.90
quatro_formaggi_price = 14.90
quatro_carni_price = 14.90
della_casa_price = 12.90
napoli_price = 9.90
ids_list = []

def calculate_price(pizza_amount, price):
    total = 0
    total = round((pizza_amount*price), 2)
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


@app.route('/returnjsonPepperoni', methods=['POST'])
def ReturnPepperoni():
    global raw_pepperoni_data
    
    raw_pepperoni_data = request.get_json()

    return "OK"

@app.route('/returnjsonQuatroFormaggi', methods=['POST'])
def ReturnQuatroFormaggi():
    global raw_quatro_formaggi_data
    
    raw_quatro_formaggi_data = request.get_json()
    print(raw_quatro_formaggi_data)

    return "OK"

@app.route('/returnjsonProsciuttoCrudo', methods=['POST'])
def ReturnProsciuttoCrudo():
    global raw_prosciutto_crudo_data
    
    raw_prosciutto_crudo_data = request.get_json()

    return "OK"

@app.route('/returnjsonQuatroCarni', methods=['POST'])
def ReturnQuatroCarni():
    global raw_quatro_carni_data
    
    raw_quatro_carni_data = request.get_json()

    return "OK"

@app.route('/returnjsonDellaCasa', methods=['POST'])
def ReturnDellaCassa():
    global raw_della_casa_data
    
    raw_della_casa_data = request.get_json()

    return "OK"

@app.route('/returnjsonNapoli', methods=['POST'])
def ReturnNapoli():
    global raw_napoli_data
    
    raw_napoli_data = request.get_json()

    return "OK"


@app.route('/orderDone', methods=['POST'])
def ReturnOrderDataDone():
    global ID_order_done
    
    ID_order_done = request.get_json()

    return "OK"


@app.route("/table_number", methods=['POST'])
def get_table_number():
    global table_number
    table_number = request.form['table_number']

    return redirect('/confirmation_page')


@app.route("/")
def home_page():
    global raw_pepperoni_data, raw_prosciutto_crudo_data, raw_quatro_formaggi_data, raw_quatro_carni_data, raw_della_casa_data, raw_napoli_data
    raw_pepperoni_data, raw_prosciutto_crudo_data, raw_quatro_formaggi_data, raw_quatro_carni_data, raw_della_casa_data, raw_napoli_data = {}, {}, {}, {}, {}, {}

    return render_template("index.html")


@app.route("/shopping_cart")
def shopping_cart_page():
    global raw_order_data
    raw_order_data = raw_pepperoni_data | raw_quatro_formaggi_data | raw_prosciutto_crudo_data | raw_quatro_carni_data | raw_della_casa_data  | raw_napoli_data 

    totals = {}
    if 'Pepperoni' in raw_order_data.keys():
        totals['total_pepperoni_price'] = calculate_price(raw_order_data['Pepperoni'], pepperoni_price)
    if 'Prosciutto Crudo' in raw_order_data.keys():
        totals['total_prosciutto_crudo_price'] = calculate_price(raw_order_data['Prosciutto Crudo'], prosciutto_crudo_price)
    if 'Quatro Carni' in raw_order_data.keys():
        totals['total_quatro_carni_price'] = calculate_price(raw_order_data['Quatro Carni'], quatro_carni_price)
    if 'Napoli' in raw_order_data.keys():
        totals['total_napoli_price'] = calculate_price(raw_order_data['Napoli'], napoli_price)
    if 'Della Casa' in raw_order_data.keys():
        totals['total_della_casa_price'] = calculate_price(raw_order_data['Della Casa'], della_casa_price)
    if 'Quatro Formaggi' in raw_order_data.keys():
        totals['total_quatro_formaggi_price'] = calculate_price(raw_order_data['Quatro Formaggi'], quatro_formaggi_price)

    total_price = sum(totals.values())

    return render_template("cart.html", raw_order_data=raw_order_data, totals = totals, total_price = total_price)

@app.route("/confirmation_page")
def confirmation_page():
    global id, general_data_list, order_list, ID_order_done
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

    ID_order_done = {}

    return render_template("confirmation_page.html", order=order, displayed_general_data=displayed_general_data)

@app.route("/luigi")
def luigiview():
    global list_length
    list_length = len(general_data_list)
    

    return render_template("luigiview.html", general_data_list=general_data_list, order_list=order_list, list_length = list_length)

@app.route("/mario")
def marioview():
    global ID_order_done
    list_length = len(general_data_list)
    
    if not ID_order_done:
        pass
    else:
        ids_list.append(str(ID_order_done["ID"]))
    # print("IDS list:", ids_list)
    

    return render_template("marioview.html", general_data_list=general_data_list, order_list=order_list, list_length = list_length, ids_list = ids_list, ID_order_done = ID_order_done)

if __name__ == '__main__':
    app.run()
