from flask import Flask,url_for,request


app = Flask(__name__)

def do_the_login():
    return '這是post'

def show_the_login_form():
    return '這是get'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
if __name__ == '__main__':
    app.run()