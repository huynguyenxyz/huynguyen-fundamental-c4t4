from flask import Flask, render_template

app = Flask(__name__)

class Favor():
    def __init__(self, h, i, l):
        self.hobby= h
        self.favpicture = i
        self.link = l
hobby1= Favor('league of legends',
'http://news.cdn.leagueoflegends.com/public/images/misc/GameBox.jpg',
'https://play.na.leagueoflegends.com/en_US'
)
hobby2 = Favor('Naruto',
'http://i.imacdn.com/vg/2015/05/naruto-dattebayo-large-1432284981.jpg',
'http://vuighe.net/tim-kiem/Naruto'
)
hobby3 = Favor('Harry Potter',
'http://cdn.collider.com/wp-content/uploads/harry-potter-deathly-hallows-book-cover.jpg',
'https://www.youtube.com/watch?v=Htaj3o3JD8I')
hobby_list = [hobby1, hobby2, hobby3] 
@app.route("/favorate")
def favor():
    return render_template('favor.html',favorate = hobby_list)
#run app
if __name__ == '__main__':
    app.run(debug=True)