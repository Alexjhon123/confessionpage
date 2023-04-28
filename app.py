from flask import Flask,render_template,request


app=Flask(__name__)
conf_essions={}
@app.route('/',methods=['get','post'])
def index():
    return render_template('index.html')

@app.route('/submitconf',methods=['post'])
def submit():
    name=request.form.get("name")
    confessions_from_user=request.form.get("confession")
    conf_essions[name]=confessions_from_user
    return render_template("conf_ent.html")

@app.route('/viewconf')
def view():
    return render_template('view.html',conf_essions=conf_essions)

