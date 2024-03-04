import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import  login_required,coupon_codes,checker

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


db = SQL("sqlite:///shop.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/fruits")
@login_required
def fruits():
    category = db.execute("SELECT * FROM category WHERE id = 1")
    product  = db.execute("SELECT * FROM items WHERE category_id = 1")
    return render_template("fruits.html", product=product,category=category)

@app.route("/vegetables")
@login_required
def vegetables():
    category = db.execute("SELECT * FROM category WHERE id = 2")
    product  = db.execute("SELECT * FROM items WHERE category_id = 2")
    return render_template("fruits.html", product=product,category=category)

@app.route("/pulses")
@login_required
def pulses():
    category = db.execute("SELECT * FROM category WHERE id = 3")
    product  = db.execute("SELECT * FROM items WHERE category_id = 3")
    return render_template("fruits.html", product=product,category=category)

@app.route("/cereals")
@login_required
def cereals():
    category = db.execute("SELECT * FROM category WHERE id = 4")
    product  = db.execute("SELECT * FROM items WHERE category_id = 4")
    return render_template("fruits.html", product=product,category=category)

@app.route("/meat_and_fish")
@login_required
def meat_and_fish():
    category = db.execute("SELECT * FROM category WHERE id = 5")
    product  = db.execute("SELECT * FROM items WHERE category_id = 5")
    return render_template("fruits.html", product=product,category=category)


@app.route("/<item>")
@login_required
def items(item):
        things = db.execute("SELECT * FROM items WHERE name=?",item)
        category = db.execute("SELECT * FROM category WHERE id = (SELECT category_id FROM items WHERE name = ?)",item)
        return render_template("item.html",things=things)


@app.route("/buy",methods=["GET","POST"])
@login_required
def buy():
     if request.method == "POST":
          items = db.execute("SELECT name FROM items")
          for item in items:
               if request.form.get(f"{item.get('name')}"):
                   name = item.get('name')
                   number = request.form.get(f"{item.get('name')}")
                   p = db.execute("SELECT * FROM items WHERE name = ?",name)
                   price = int(p[0]['price'])
                   bought = db.execute("SELECT * FROM bought WHERE user_id = ? AND name = ?",session["user_id"],name)
                   user_id = session["user_id"]
                   if bought:
                      number = int(number) + int(bought[0]['number'])
                      total = int( int(number) * price )
                      db.execute("UPDATE bought SET number = ?,total = ? WHERE id = ?",number,total,bought[0]['id'])
                      return render_template("buy.html",number=number,p=p)
                   else:
                          total = int( int(number) * price )
                          db.execute("INSERT INTO bought (user_id,name,price,number,total) VALUES (?,?,?,?,?)",user_id,name,price,number,total)
                          return render_template("buy.html",number=number,p=p)
          return "ERROR"

     else:
          return 0

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()


    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if not rows:
            return render_template("login.html",message="Account doesn't exist")

        elif not check_password_hash(rows[0]["hash"], request.form.get("password")):
             return render_template("login.html",message="Incorrect password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    elif request.method == "GET":
        return render_template("login.html",message="")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()

    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        people = db.execute("SELECT username FROM users")
        if (username in people):
               return render_template("register.html",message="Username already taken")
        hash1 = generate_password_hash(password)
        db.execute("INSERT INTO users(username, hash) VALUES(?,?)",username, hash1)
        print(username,hash1)
        id1 = db.execute("SELECT id FROM users WHERE username = ?", username)
        session["user_id"] = id1[0]['id']
        return redirect("/")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")



@app.route("/cart",methods=["GET","POST"])
@login_required
def cart():
     if request.method == "GET":
          products = db.execute("SELECT * FROM bought where user_id = ?",session["user_id"])
          sum1 = db.execute("SELECT SUM(total) AS sum FROM bought WHERE user_id = ? ",session["user_id"])[0]['sum']
          return render_template("/cart.html",products=products,sum1=sum1)

     elif request.method == "POST":
          sum1 = int(db.execute("SELECT SUM(total) AS sum FROM bought WHERE user_id = ? ",session["user_id"])[0]['sum'])
          if request.form.get("coupon"):
                 code = request.form.get("coupon")
                 if coupon_codes(code):
                      sum1 = sum1 - int(sum1 * 0.1)
                      if db.execute("SELECT * FROM cost WHERE user_id = ?",session["user_id"]):
                            db.execute("UPDATE cost SET total = ? WHERE user_id = ?",sum1,session["user_id"])
                            return render_template("paycheck.html",message="COUPON REDEEMED 😊",sum=sum1)
                      else:
                           db.execute("INSERT INTO cost (user_id,total) VALUES (?,?)",session["user_id"],sum1)
                           return render_template("paycheck.html",message="COUPON REDEEMED 😊",sum=sum1)
                 else:
                      if db.execute("SELECT * FROM cost WHERE user_id = ?",session["user_id"]):
                           db.execute("UPDATE cost SET total = ? WHERE user_id = ?",sum1,session["user_id"])
                           return render_template("paycheck.html",message="COUPON NOT FOUND 😓",sum=sum1)
                      else:
                           db.execute("INSERT INTO cost (user_id,total) VALUES (?,?)",session["user_id"],sum1)
                           return render_template("paycheck.html",message="COUPON NOT FOUND 😓",sum=sum1)
          else:
                if db.execute("SELECT * FROM cost WHERE user_id = ?",session["user_id"]):
                     db.execute("UPDATE cost SET total = ? WHERE user_id = ?",sum1,session["user_id"])
                     return render_template("paycheck.html",message="COUPON NOT ENTERED",sum=sum1)
                else:
                     db.execute("INSERT INTO cost (user_id,total) VALUES (?,?)",session["user_id"],sum1)
                     return render_template("paycheck.html",message="COUPON NOT ENTERED",sum=sum1)



@app.route("/paycheck",methods=["GET","POST"])
@login_required
def paycheck():
     if request.method == "POST":
          paid = int(request.form.get("paycheck"))
          total = int(db.execute("SELECT total FROM cost WHERE user_id = ?",session["user_id"])[0]['total'])
          while (checker(paid,total)  == 1):
                  new = total - paid
                  db.execute("UPDATE cost SET total = ? WHERE user_id = ?",new,session["user_id"])
                  return render_template("paycheck.html",message ="Not suffecient",sum=new)
          if checker(paid,total) == 2:
               products = db.execute("SELECT * FROM bought WHERE user_id = ?",session["user_id"])
               db.execute("DELETE FROM cost WHERE user_id = ?",session["user_id"])
               db.execute("DELETE FROM bought WHERE user_id = ?",session["user_id"])
               return render_template("bill.html",message = "Purchase success",products=products )
          elif checker(paid,total) == 0:
               products = db.execute("SELECT * FROM bought WHERE user_id = ?",session["user_id"])
               new = paid - total
               db.execute("DELETE FROM cost WHERE user_id = ?",session["user_id"])
               db.execute("DELETE FROM bought WHERE user_id = ?",session["user_id"])
               return render_template("bill.html",message=f"Purchase success, Seems you paid extra. Here's your ₹{new}",products=products)


@app.route("/feedback",methods=["GET","POST"])
def feedback():
     if request.method == "POST":
          feedback=request.form.get("feedback")
          with open("feedback.txt",'a') as fp:
               fp.write(feedback)
               fp.write("\n")
               return render_template("thank.html")
     else:
          return render_template("feedback.html")