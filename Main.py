from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route("/") 
def home ():
    return render_template("inicio.html")
@app.route("/inicio.html") 
def inicio ():
    return render_template("inicio.html")
@app.route("/contato.html") 
def homepage ():
    return render_template("contato.html")
@app.route("/sobre.html") 
def sobre ():
    return render_template("sobre.html")
if __name__ == "__main__":
    app.run(debug = True)