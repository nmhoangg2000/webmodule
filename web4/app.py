from flask import Flask, render_template, request, session, redirect
from models.character import Character
from models.user import User
import mlab



app = Flask(__name__)
app.config["SECRET_KEY"] = "-fnW6EtUpyj6FY49NuDbLR9y9u8xsfYrbfPdhwrk"

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
    if "token" in session:    
                #1 get all characters (database)
                character_list = Character.objects()
                #2 render
                return render_template("characters.html", character_list= character_list)  
    else:
            return redirect("/login?next=/characters")

@app.route("/login", methods=["GET", "POST"])
def login():
        if request.method == "GET":
                return render_template("login_form.html")
        elif request.method == "POST":
                form = request.form
                username = form["username"]
                password = form["password"]

                found_user = User.objects(username=username).first()
                if found_user is None:
                        return "user not found"
                elif found_user.password != password:
                        return "invalid password"
                else:
                        session["token"] = username
                        next= request.args.get("next")
                        if next is None or next =="":
                                return "Logged in successfully"     
                        else:
                                return redirect(next)
                

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

@app.route("/logout")
def logout():
        del session["token"]
        return redirect("/login")    
@app.route("/posts")
def posts():
        if "token" not in session:
                return redirect("/login?next=/posts")
        else:
                username = session["token"]
                        
if __name__ == '__main__':
  app.run(debug=True)