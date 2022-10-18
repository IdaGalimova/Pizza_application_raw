from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

pepperoni_amount = 0
data = "NULL"


@app.route('/returnjson1', methods = ['POST'])
def ReturnJSON():
    global order_info, data, pepperoni_amount
    order_info = {}
    data = request.get_json()
    print(data['pepperoni_amount'])

# {'pepperoni_amount': 3}

    order_info['pepperoni_amount'] = data['pepperoni_amount']
    
    return "OK"

@app.route("/")
def home_page():

    return render_template("home.html", pepperoni_amount = pepperoni_amount)

@app.route("/shopping_cart")
def shopping_cart_page():
    for key, value in order_info.items():
        print(key, value)
    # if order_info = 

    return render_template("shopping_cart.html", order_info = order_info)



if __name__ == '__main__':
    app.run()