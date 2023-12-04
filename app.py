from flask import Flask,render_template,request



app = Flask(__name__)


list_logins = "Mateus","Jose"
def validar_login(name):
    if name in list_logins:
        return True
    return False



@app.route("/",methods=["GET"])
@app.route("/<iuser>",methods=["POST","GET"])
def index(iuser=None):
    if request.method == "POST":
        username = iuser
        print(f"O seu nome é: {username}")
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True,port=8080)