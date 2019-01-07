from flask import Flask, render_template
app = Flask(__name__)

@app.route("/names")
def names():
    name_list=["Huy","Dũng","Looong","Hà cứt gà"]
    return render_template("name_list.html",
                            names= name_list)


food_list = [
     {
      "name": "phở",
      "image":"https://media.cooky.vn/recipe/g1/3315/s800x500/recipe3315-635754951948774481.jpg",
      "link":  "https://www.google.com/search?q=ph%E1%BB%9F&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjr7pir4dbfAhXJfXAKHdLFAHUQ_AUIDigB&biw=1536&bih=754#imgrc=AYOsOCLI6PRmhM:",
      "ytb": "3tNNK5Pv7co&t=448s"
    },
     {
      "name": "bún riêu",
      "image":"http://www.monngon.tv/uploads/images/2017/04/18/8c82d5cfa5897cdeef14c62ae7de44e6-cach-nau-bun-rieu-slide.jpg",
      "link":  "https://www.google.com/search?q=b%C3%BAn+ri%C3%AAu&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiVuL3a4dbfAhUWMt4KHTF7B1wQ_AUIDigB&biw=1536&bih=754#imgrc=DhFNt0tvMaM4aM:"
    },
     {
      "name": "thịt chó",
      "image":"https://dantricdn.com/2018/9/15/co-dau-doi-ly-hon-vi-nha-chong-lam-tiec-cuoi-bang-thit-cho-1536986207809731598543.jpg",
      "link":  "https://www.google.com/search?biw=1536&bih=754&tbm=isch&sa=1&ei=RbMwXNmAFcbBoAS624Ag&q=th%E1%BB%8Bt+ch%C3%B3&oq=th%E1%BB%8Bt+ch%C3%B3&gs_l=img.3..0l10.33075.35785..35974...3.0..5.103.1598.17j1......2....1..gws-wiz-img.....0..0i67j35i39.ainALMZZV54#imgrc=mkQQ-xoZ0cFAZM:"
    }
]

@app.route("/food_items")
def food():
   
    return render_template("food.html",
                            food_items = food_list)

@app.route("/food_detail/<index>")
def food_detail(index):
    food_item = food_items[index]
    return render_template("food_detail.html",
                            food_items = food_items)
if __name__ == '__main__':
  app.run(debug=True)