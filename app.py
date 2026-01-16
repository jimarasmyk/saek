from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    msg = None
    if request.method == "POST":
        if request.form["user"] == "admin":
            msg = "Καλώς ήρθες admin"
        elif request.form["user"] == "saek":
            msg = "Καλημέρα ΣΑΕΚ Κηφισιάς"
        else:
            msg = "Λάθος χρήστης"
    return render_template("index.html", msg=msg)

if __name__ == "__main__":
 app.run()
