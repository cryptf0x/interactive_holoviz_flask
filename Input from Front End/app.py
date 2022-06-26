from re import template
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="template")

@app.route('/', methods=["GET", "POST"])
def homepage():
    return render_template("form.html")

@app.route('/submit_input', methods=["GET", "POST"])
def submit_form():
    if request.method == "POST":
        said_ids = request.form.get("said_ids")
        from_date = request.form.get("from_date")
        to_date = request.form.get("to_date")
    print(said_ids)
    print(from_date)
    print(to_date)
    return render_template("submission.html")

if __name__ == '__main__':
    app.run()
