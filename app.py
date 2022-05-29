from flask import Flask,render_template,request
import numpy as np
import pickle

model = pickle.load(open(r'artifacts/model.pkl','rb'))



app = Flask(__name__)

@app.route('/')
def index():
    print("we are in index deaful;t api")
    return render_template('index.html')

@app.route('/prediction',methods = ['GET','POST'])
def prediction():

    
    gender = int(request.form['gender'])
    married = int(request.form['married'])
    dependents = int(request.form['dependents'])
    education = int(request.form['education'])
    self_employed = int(request.form['self_employed'])
    loan_term = int(request.form['loan_term'])
    credit_history = int(request.form['credit_history'])
    property_area = int(request.form['property_area'])
    loan_amount = int(request.form['loan_amount'])
    log_loan_amount = np.log(loan_amount)
    app_income = int(request.form['app_income'])
    co_app_income = int(request.form['co_app_income'])
    log_total_income = np.log(app_income+co_app_income)

    data = [[gender,married,dependents,education,self_employed,loan_term,credit_history,property_area,log_loan_amount,log_total_income]]

    result = model.predict(data)
    
    print(result)
    if result[0]== 1:
        result = "LOAN APPROVE"
    else:
        result = "LOAN REJECTED"
    print(result)

    return render_template('index.html',loan_result=result)




if __name__ =="__main__":
    app.run(host='0.0.0.0', port=8080 , debug=True)