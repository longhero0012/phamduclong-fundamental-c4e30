from flask import Flask, render_template,request
app = Flask(__name__)
profile= [{
        "user":"phamlong1",
        "pass":"1"
    },{
        "user":"phamlong2",
        "pass":"2"
    },{
        "user":"phamlong3",
        "pass":"3"
    }]

@app.route('/',methods=["POST"])
def logins():
    user = request.form.get("tai_khoan")
    password = request.form.get("mat_khau")
    check = False
    for v in profile :
        if user == v["user"] and password == v ["pass"] :
            check = True
    if check == True:
            return render_template("successful.html")
    else :
            return render_template("falied.html")

    
@app.route('/',methods=["GET"])
def get():
    return render_template('login.html',data = profile)
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 