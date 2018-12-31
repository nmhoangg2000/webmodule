from flask import Flask, render_template
app = Flask(__name__)

@app.route("/bmi/<int:w>/<int:h>")
def bmi(w,h):
    BMI = w/(h/100*h/100)
    return render_template("bmi.html",
                            bmi = BMI)

if __name__ == '__main__':
  app.run(debug=True)