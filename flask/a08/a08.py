from flask import Flask,url_for,request,render_template


app = Flask(__name__)

def do_the_login():
    user = request.form["nm"]
    return render_template("index.html",user=user)

def show_the_login_form():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
if __name__ == '__main__':
    app.run()