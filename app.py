from flask import Flask, render_template
import sys

application = Flask(__name__)

@application.route("/") # /를 만날 때 마다 hello()를 실행
def hello() :
    return render_template("index.html")

if __name__ == "__main__":
    application.run(host='0.0.0.0',debug=True)