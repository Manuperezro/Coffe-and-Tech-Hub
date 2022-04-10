from flask import Flask, render_template, url_for, session
import requests 


app = Flask(__name__)
# route == link == url
app.secret_key= "My_Super_Secret_Key"


@app.route("/")
def main():
    # articles = [{"title1":"title1", "text1":"text1"},{"title2":"title2", "text2":"text2"},{"title3":"title3", "text3":"text3"}]
    rawData = requests.get("https://newsapi.org/v2/top-headlines?country=us&language=en&apiKey=bf0b73effbfa4f2991187cc0522a89fd")
    headlines = rawData.json()
    sessionDescriptions = {} 
    for headline in headlines['articles']:
        # {2022-04-08T23:45:06Z: "Description", 2022-03-08T23:42:05z: "Description",} 
        sessionDescriptions[headline['publishedAt']] = headline['description']   
    # store the description in flask session
    session['description'] = sessionDescriptions    
    # to return the jason Object un comment retunr headlines 
    # return headlines
    return render_template("home.html", headlines=headlines)


@app.route("/<category>")
def category(category):
    # articles = [{"title":"title1", "text":"text1"},{"title":"title2", "text":"text2"},{"title":"title3", "text":"text3"}]
    rawData = requests.get("https://newsapi.org/v2/top-headlines?category="+category+"&country=us&apiKey=b026b6dc8ae1444989e73d7b1dfdbe5d")
    headlines = rawData.json()
    sessionUrl = {} # {67678987:"gvghjgjhghh",87687876:"ghfhjghkjghj","68768":"ghfhfgh"}
    for headline in headlines['articles']:
        sessionUrl[headline['publishedAt']] = headline['url']  
        # {'2020-09-09T07:04:00Z':"fhhghfhgfh",'2020-09-09T07:04:00Z':"gfhgfhgfhfj"}
    # store the descriptions in flask session
    session['url'] = sessionUrl 
    # return headlines
    return render_template("category.html", headlines=headlines)


# @app.route("/single/<publishedAt>")
# def single(publishedAt):
#     """
#     Open a new page to read the full article from a card
#     """
#     return render_template('single.html', publishedAt=publishedAt)


if __name__ == "__main__":
    app.run(debug=True)