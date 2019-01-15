from flask import Flask, render_template, request
import mlab
from models.bike import New_bike

mlab.connect()
app = Flask(__name__)

@app.route("/new_bike", methods=["GET", "POST"])
def new_bike():
    if request.method == "GET":
        return render_template("bike.html")
    elif request.method == "POST":
        form = request.form
        n = New_bike(model=form["model"], daily_fee=form["daily-fee"], image=form["image"], year=form["year"])
        n.save()
        return "Gotcha!!!"
if __name__ == "__main__":
    app.run(debug=True)