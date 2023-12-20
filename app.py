from flask import Flask,render_template,redirect


app = Flask(__name__)



ROTAS = ("home","sobre","projetos","contato")


@app.route("/")
def home():
    return render_template("index.html",routes=ROTAS)


@app.route("/sobre")
def sobre():
    return render_template("sobre.html",routes=ROTAS)

@app.route("/contato")
def contato():
    return render_template("contato.html",routes=ROTAS)

@app.route("/projetos")
def projetos():
    return render_template("projeto.html",routes=ROTAS)

if __name__ == "__main__":
    app.run(debug=True)