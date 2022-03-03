from flask import Flask, render_template,session,redirect, request

app = Flask(__name__)
app.secret_key = 'claveSecreta'

@app.route('/')
def index():
    if 'contador' in session:
        session["contador"] += 1
    else:
        session["contador"] = 1
    return render_template("index.html", contador = session["contador"])

@app.route('/destroy_session')
def destroySession():
    session.clear()
    return redirect("/")

@app.route('/AddTwo')
def addTwo():
    if 'contador' in session:
        session["contador"] += 2
    return render_template("index.html", contador = session["contador"])

@app.route('/AumentarX', methods=['POST'])
def AumentarX():
    print(request.form)
    if 'contador' in session:
        session["contador"] += int(request.form['txt_cantidad'])
    return render_template("index.html", contador = session["contador"])

if __name__=="__main__":
    app.run(debug=True)