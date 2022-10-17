from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

pepperoni_amount = 0
data = "NULL"
order_info = {}


@app.route('/returnjson1', methods = ['POST'])
def ReturnJSON():
    global data, pepperoni_amount
    data = request.get_json()
    print(data['pepperoni_amount'])
    order_info['pepperoni_amount'] = data['pepperoni_amount']
    
    return "OK"

@app.route("/")
def manual_page():

    return render_template("home.html", pepperoni_amount = pepperoni_amount, order_info = order_info)


@app.route('/handle_data', methods=['POST'])
def handle_data():
    pizza_amount = request.form['pizza_amount']
    print(pizza_amount)
    
    return "OK"


if __name__ == '__main__':
    app.run()