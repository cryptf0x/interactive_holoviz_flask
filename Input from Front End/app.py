from re import template
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="template")

@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        return "Your name is " + first_name + " " + last_name
    else:
        return render_template("form.html")

if __name__ == '__main__':
    app.run()