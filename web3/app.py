from flask import Flask, render_template, request
from models.character import Character
import mlab
app = Flask(__name__)
mlab.connect()

#character.objects()

@app.route('/add_character', methods=['GET','POST'])
def add_character():
    #1: gửi form(GET)
    if request.method == "GET":
        return render_template("character_form.html")
    elif request.method == "POST":
  #4: nhận form => Lưu (POST)
        form = request.form 
        name = form["name"]
        image = form["image"]
        rate = form["rate"]
        print(name, image, rate)
        new_character = Character(name=name, image=image, rate=rate)
        new_character.save()
        return "Gotcha"
#list
@app.route('/characters') #hien thi tat ca cac nhan vat
def characters():
    #1 get all characters (database)
    character_list = Character.objects()
    #2 render
    return render_template("characters.html", character_list= character_list)  

@app.route("/character/<given_id>")
def character_detail(id): #one
    #1 get one character, based on given id
    # character = Character.objects(id=gievn_id).first()
    character = Character.objects().with_id(given_id)
    if character is None:
        return "Not found"
    else:    
    #2 render: template + data
    return render_template("character_detail.html", character=character)

    

if __name__ == '__main__':
  app.run(debug=True)