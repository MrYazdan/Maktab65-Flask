from flask import redirect, url_for, request


# @app.route('/hello')
def say_hello(name):
    return f"<center><h1 style='color: orangered'>Hi {name} ^_^</h1></center>"


# @app.route('/hi?name=alireza')
def say_hello_by_query():
    # name = "Kokab"
    # if request.args['name']:
    #     name = request.args['name']

    # name = request.args['name'] if request.args['name'] else "Kokab"

    name = request.args.get('name', 'Kokab')
    print(name)
    return f"<center><h1 style='color: orangered'>Hi {name} ^_^</h1></center>"


# sum/num1/num2
def summary(num1, num2):
    return f"<center><h1 style='color: green'>Sum of {num1} + {num2} = {num1 + num2} !</h1></center>"


# pow/num1/num2
def power(num1, num2):
    return f"<center><h1 style='color: blue'>Power of {num1} ** {num2} = {num1 ** num2} !</h1></center>"


def google_search(text):
    return redirect(f"https://www.google.com/search?q={text}")


def home():
    return f"""
    <center>
    <ul style='color: black'>
        <li><a href='{url_for('home')}'>Home</a></li>
        <li><a href='{url_for('hi')}'>Say hello</a></li>
        <li><a href='{url_for('search', text="iran")}'>Search it !</a></li>
        <li><a href='{url_for('method_detector')}'>Method finder</a></li>
    </ul>
    </center>
"""


def detector():
    # return f"Resquest by {request.method} method!"
    if request.method == "POST":
        return f"Resquest by POST method!"
    elif request.method == "GET":
        return f"Salaaaaaaam !"


def request_info():
    return f"""
<ul>
    <li><b>method</b> : {request.method}</li>
    <li><b>url</b> : {request.url}</li>
    <li><b>args</b> : {request.args}</li>
    <li><b>headers</b> : {request.headers}</li>
</ul>
    """
