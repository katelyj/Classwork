from flask import Flask, render_template, request

ramirez = Flask(__name__)

@ramirez.route("/")
def home():
    return render_template("form.html")

@ramirez.route("/one")
def one():
    return render_template("form1.html")

if __name__ == '__main__':
    ramirez.debug = True
    ramirez.run()
