from flask import Flask, render_template, url_for, session
import requests 


app = Flask(__name__)
# route == link == url
app.secret_key= "My_Super_Secret_Key"


@app.route("/")
def main():
    # articles = [{"title1":"title1", "text1":"text1"},{"title2":"title2", "text2":"text2"},{"title3":"title3", "text3":"text3"}]
    rawData = requests.get("https://newsapi.org/v2/everything?sources=techcrunch&apiKey=bf0b73effbfa4f2991187cc0522a89fd")
    headlines = rawData.json()
    sessionDescriptions = {} 
    for headline in headlines['articles']:
        # {2022-04-08T23:45:06Z: "Description", 2022-03-08T23:42:05z: "Description",} 
        sessionDescriptions[headline['publishedAt']] = headline['content']   
    # store the description in flask session
    session['content'] = sessionDescriptions    
    # to return the jason Object un comment retunr headlines 
    return headlines
    return render_template("home.html", headlines=headlines)


@app.route("/")
def main():
    # articles = [{"title1":"title1", "text1":"text1"},{"title2":"title2", "text2":"text2"},{"title3":"title3", "text3":"text3"}]
    rawData = requests.get("https://newsapi.org/v2/everything?category=sports&sources=techcrunch&apiKey=bf0b73effbfa4f2991187cc0522a89fd")
    headlines = rawData.json()
    sessionDescriptions = {} 
    for headline in headlines['articles']:
        # {2022-04-08T23:45:06Z: "Description", 2022-03-08T23:42:05z: "Description",} 
        sessionDescriptions[headline['publishedAt']] = headline['content']   
    # store the description in flask session
    session['content'] = sessionDescriptions    
    # to return the jason Object un comment retunr headlines 
    return headlines
    return render_template("home.html", headlines=headlines)


@app.route("/singleNews/<publishedAt>")
def singleNews(publishedAt):
    """
    Open a new page to read the full article from a card
    """
    # return all of the sesion['descriptions'] diccionary
    descriptions = session.get("descriptions")
    # return the unique descriptions using the publishedAt "key"
    description = descriptions[publishedAt]
    return render_template('single.html', description=description)


if __name__ == "__main__":
    app.run(debug=True)