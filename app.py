from flask import Flask, render_template,request
from flask_cors import CORS
from models import create_exp,get_exp

app = Flask(__name__)

CORS(app)

@app.route('/home', methods = ['GET','POST'])

def index():
    if(request.method =='GET'):
        pass
    
    if(request.method =='POST'):
        
        date = request.form.get('Date')
        category = request.form.get('Category')
        sub_category = request.form.get('sub_category')
        expense = request.form.get('Expense')
        create_exp(date,category,sub_category,expense)


    allexpense = get_exp()

    return render_template('bootpage.html' , allexpense = allexpense)

if (__name__ == '__main__'):
    app.run(debug=True)

