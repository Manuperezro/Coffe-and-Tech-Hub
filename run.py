from flask import Flask, render_template, url_for, session, request
from flask_sqlalchemy import SQLAlchemy
from flask import redirect
import os
import requests
# route == link == urls
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key= "My_Super_Secret_Key"
db = SQLAlchemy(app)



class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
class Ideas(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))

# class List(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     Idea_list =  Ideas.query.all()

# News Api routes--

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
    return render_template("category.html", headlines=headlines)
# Ideas routes--   
@app.route("/ideas.html")
def Idea():
    """
    Open a new page to the Ideas page
    """
    #show all todos:
    ideas_list = Ideas.query.all()
    print(ideas_list)
    return render_template("ideas.html", ideas_list=ideas_list)


@app.route("/add_idea", methods=["POST"])
def add_idea():
    # add new idea to the list
    title = request.form.get("idea_title")
    new_idea = Idea(title=title, complete=False)
    db.session.add(new_idea)
    db.session.commit()
    return redirect(url_for("idea"))   
# Todo App routes--
@app.route("/todo.html")
def todo():
    """
    Open a new page to the todo list page
    """
    #show all todos:
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template("todo.html", todo_list=todo_list)


@app.route("/list")
def ideas_list():
    # Show the list of todos list
    title = request.form.get("todo_title")
    new_todo = Todo(title=title, complete=False)
    return redirect(url_for("Ideas", ideas_list=ideas_list))


@app.route("/add", methods=["POST"])
def add():
    # add new todo to the list
    title = request.form.get("todo_title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("todo"))

@app.route("/complete/<int:todo_id>")
def complete(todo_id):
    # add new todo to the list
    # mark as completed the todos
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("todo"))
    

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    # add new todo to the list
    # deleted a todo
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todo"))
    
if __name__ == "__main__":
    db.create_all()
    app.run(
        host=os.environ.get("IP","0.0.0.0"),
        port=int(os.environ.get("PORT","5000")),
        debug=True)