from flask import Flask, render_template
app = Flask(__name__)

#template rendering


@app.route('/characters')
def characters():
    # c = {
    #   "name": "Thanos",
    #   "image":"https://www.sideshowtoy.com/wp-content/uploads/2018/04/marvel-avengers-infinity-war-thanos-sixth-scale-figure-hot-toys-feature-903429-1.jpg",
    #   "link":  "https://www.google.com/search?biw=1536&bih=706&tbm=isch&sa=1&ei=zKYwXI37N4jN-QbVrquQAQ&q=thanos&oq=thanos&gs_l=img.3..0l10.7175.9926..10301...0.0..2.103.1380.16j1......1....1..gws-wiz-img.....0..35i39j0i19j0i30i19j0i67.1HUTZSEtQts#imgrc=jQDI0E1bHEoVwM:"
    # }
    c_list = [
         {
      "name": "uncle ben",
      "image":"https://www.sideshowtoy.com/wp-content/uploads/2018/04/marvel-avengers-infinity-war-thanos-sixth-scale-figure-hot-toys-feature-903429-1.jpg",
      "link":  "https://www.google.com/search?biw=1536&bih=706&tbm=isch&sa=1&ei=zKYwXI37N4jN-QbVrquQAQ&q=thanos&oq=thanos&gs_l=img.3..0l10.7175.9926..10301...0.0..2.103.1380.16j1......1....1..gws-wiz-img.....0..35i39j0i19j0i30i19j0i67.1HUTZSEtQts#imgrc=jQDI0E1bHEoVwM:"
    },
     {
      "name": "star lord",
      "image":"https://www.sideshowtoy.com/wp-content/uploads/2018/04/marvel-avengers-infinity-war-thanos-sixth-scale-figure-hot-toys-feature-903429-1.jpg",
      "link":  "https://www.google.com/search?biw=1536&bih=706&tbm=isch&sa=1&ei=zKYwXI37N4jN-QbVrquQAQ&q=thanos&oq=thanos&gs_l=img.3..0l10.7175.9926..10301...0.0..2.103.1380.16j1......1....1..gws-wiz-img.....0..35i39j0i19j0i30i19j0i67.1HUTZSEtQts#imgrc=jQDI0E1bHEoVwM:"
    },
     {
      "name": "captain marvel",
      "image":"https://www.sideshowtoy.com/wp-content/uploads/2018/04/marvel-avengers-infinity-war-thanos-sixth-scale-figure-hot-toys-feature-903429-1.jpg",
      "link":  "https://www.google.com/search?biw=1536&bih=706&tbm=isch&sa=1&ei=zKYwXI37N4jN-QbVrquQAQ&q=thanos&oq=thanos&gs_l=img.3..0l10.7175.9926..10301...0.0..2.103.1380.16j1......1....1..gws-wiz-img.....0..35i39j0i19j0i30i19j0i67.1HUTZSEtQts#imgrc=jQDI0E1bHEoVwM:"
    }
    ]
    return render_template("characters_list.html", 
                           character_list=c_list)
  

if __name__ == '__main__':
  app.run(debug=True)