from flask import Flask, render_template, request
import sys

application = Flask(__name__)

@application.route("/") # /를 만날 때 마다 hello()를 실행
def hello() :
    return render_template("index.html")

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

@application.route("/submit_item")
def reg_item_submit():
    name=request.args.get("name")
    seller=request.args.get("seller")
    addr=request.args.get("addr")
    email=request.args.get("email")
    category=request.args.get("category")
    card=request.args.get("card")
    status=request.args.get("status")
    phone=request.args.get("phone")
    print(name,seller,addr,email,category,card,status,phone)
    return render_template("reg_items.html")

#@application.route("/submit_item_post", methods=['POST'])
#def reg_item_submit_post():
#    image_file=request.files["file"]
#    image_file.save("static/images/{}".format(image_file.filename))
    
#    data=request.form
#    return render_template("submit_item_result.html", data=data,
#img_path="static/images/{}".format(image_file.filename))

@application.route("/submit_item_post", methods=['POST'])
def reg_item_submit_post():
    # Extract data from the form
    name = request.form.get("name")
    seller = request.form.get("seller")
    addr = request.form.get("addr")
    email = request.form.get("email")
    category = request.form.get("category")
    card = request.form.get("card")
    status = request.form.get("status")
    phone = request.form.get("phone")
    
    # Print the form data to the terminal
    print(name, seller, addr, email, category, card, status, phone)
    
    # Save the uploaded file
    image_file = request.files["file"]
    image_file.save("static/images/{}".format(image_file.filename))
    
    # Pass data to the template
    return render_template("submit_item_result.html", data=request.form,
                           img_path="static/images/{}".format(image_file.filename))

    