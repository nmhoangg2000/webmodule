from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")  #router
def home(): #view function
    c ={
        "name": "AQUAMAN",
        "company": "DC COMICS",
        "image": "https://media.apnarm.net.au/media/images/2017/10/09/pornastar-alhgn3jrzi5m5w162p2_ct677x380.jpg",
        "abilities":["Speed", "Strength", "Reflexes", "Underwater"]
    }
    return render_template("home.html", character=c) #serve html

@app.route("/c4e")
def c4e():
    return "Code For Everyone 24"

@app.route("/hi/<name>")
def say_hi(name):
    return "Hi " + name

@app.route("/add/<num1>/<num2>")
def add(num1 , num2):
    num1 = int(num1)
    num2 = int(num2)
    s =str(num1 + num2)
    return s   


if __name__ == "__main__":
    app.run(debug=True)
