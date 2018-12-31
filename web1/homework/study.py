from flask import Flask, render_template, redirect
study = Flask(__name__)
@study.route("/about-me")
def home():
    me = {
        "name":"Nguyễn Minh Hoàng",
        "job": "Student",
        "School": "USTH",
        "Hobbies": "sports, games"
    }
    return render_template("aboutme.html",me =me)

@study.route("/school")
def school():
    return redirect(" http://techkids.vn", code= 302)
if __name__ == "__main__":
    study.run(debug=True)    