from flask import redirect, render_template, session
from functools import wraps


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def coupon_codes(code):
    with open("coupon.txt","r") as codes:
        coupon_codes_list=codes.readlines()
        list1=[]
        for i in coupon_codes_list:
            list1.append(i[0:4])
        if code in list1:
             list1.remove(code)
             with open("coupon.txt","w") as codes:
                for i in list1:
                    codes.write(f"{i}\n")
             return True
        else:
             return False

def checker(amount1,amount2):
        if amount1 > amount2:
            return 0
        elif amount1 < amount2:
            return 1
        elif amount1 == amount2:
             return 2

