from flask import Flask, render_template, request
from flask_mail import Mail

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']= 465
app.config['MAIL_USERNAME'] = 'bryanmyner88@gmail.com'
app.config['MAIL_PASSWORD'] = 'bvcictaqahvpyraz'
app.config['MAIL_USE_TLS']= False
app.config['MAIL_USE_SSL']= True
mail = Mail(app)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.errorhandler(404)  
def not_found(e): 
    return render_template("404.html") 

if __name__ == '__main__':
    app.run(debug=True)