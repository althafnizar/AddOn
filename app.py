from flask import Flask, render_template

app = Flask(__name__)  #class object

# def test(st):
# route(path)

@app.route('/test')
def hello():
    print("This route is being called!")
    return render_template("home.html")

@app.route('/about')
def about():
    name= "althaf"
    age = 45
    runs= [20,30,40,68,13]
    return render_template("index.html",name=name,age=age,runs=runs)

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/base')
def base():
    return render_template("base.html")

@app.route('/form')
def form():
    return render_template("form.html")

app.run(debug=True)