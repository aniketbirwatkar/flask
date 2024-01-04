## Create a simple flask application 

from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)

@app.route('/') 
def home () : 
    return "<h2>hello world !</h2> "

@app.route('/welcome') 
def welcome () : 
    return "Welcome to the Flask Tutorial."

@app.route('/index') 
def index () : 
    return render_template ("index.html")

@app.route('/success/<int:score>')
def success (score) : 
    return "The result is " + str(score)

@app.route('/fail/<int:score>')
def fail (score) : 
    return "You are failed and score is   " + str(score)

@app.route ('/calculate', methods=['GET','POST'])
def calculate () :
    if request.method== 'GET' : 
        return render_template ('calculate.html')
    else : 
        maths= float(request.form['maths'])
        science=  float(request.form['science'])
        history=float(request.form['history'])

        average_marks = (maths+science+history)/3

        result=""
        if average_marks>=40:
            result="success"
        else : 
            result = "fail"

        return redirect (url_for(result,score=average_marks))
            

        #return render_template ('result.html', results= average_marks)
        #You can use the result.html file if you want to proceed with render_template else you have to import the redirect and URL_for as shown above



if __name__ == "__main__":
    app.run(debug=True)