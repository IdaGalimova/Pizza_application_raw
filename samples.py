from flask import Flask, render_template, request, jsonify
import random
from time import sleep
from datetime import datetime

app = Flask(__name__)
id = 0

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

    return table, time, id



while True:
    table, time, id = generate(id)
    print(id)
    sleep(1)

# @app.route("/")
# def home_page():
    

#     return render_template("home.html")


# if __name__ == '__main__':
#     app.run()
