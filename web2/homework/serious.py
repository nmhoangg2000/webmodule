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
@app.route('/')
def home():
    return ''

@app.route('/register',methods = ['POST', 'GET'])
def result():
   if request.method == 'GET':
      return render_template("register.html")
   elif request.method == 'POST':
      form = request.form
      name = form["name"]
      email = form["email"]
      username = form["username"]
      password = form["password"]

      u = Users(name=name,email=email,username=username,password=password)
      u.save()
      return "Singed Up Successfully"
  

if __name__ == '__main__':
  app.run(debug=True)