from flask import Flask, render_template
import sys

application = Flask(__name__)

@application.route("/") # /를 만날 때 마다 hello()를 실행
def hello() :
    return render_template("index.html")

# if __name__ == "__main__":
#    application.run(host='0.0.0.0',debug=True)

@application.route("/list")
def view_list():
    return render_template("list.html")

@application.route("/review")
def view_review():
    return render_template("review.html")

@application.route("/reg_items")
def reg_item():
    return render_template("reg_items.html")

@application.route("/reg_reviews")
def reg_review():
    return render_template("reg_reviews.html")      
