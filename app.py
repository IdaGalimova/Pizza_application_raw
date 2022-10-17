from flask import Flask, render_template

app = Flask(__name__)
pepperoni_amount = 0
@app.route("/")
def manual_page():
    

    return render_template("home.html", pepperoni_amount = pepperoni_amount)


if __name__ == '__main__':
    app.run()