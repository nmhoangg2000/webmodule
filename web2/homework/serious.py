from flask import Flask,render_template,request 
import mlab  
from mongoengine import Document, StringField, IntField
mlab.connect()

class Users(Document):
  name = StringField()
  email = StringField()
  username = StringField()
  password = StringField()


app = Flask(__name__)

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)
  

if __name__ == '__main__':
  app.run(debug=True)
