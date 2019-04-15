from flask import Flask
app = Flask(__name__)


@app.route('/about-me')
def aa ():
  profile=["name : phạm đức long","work : student","school : thủy lợi university","hobbies : phay game","crush : nooooooooooo"]    
  return str(profile)
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
from flask import Flask, redirect
app = Flask(__name__)
 
 
@app.route('/school')
def hello():
  return redirect("https://mindx.edu.vn/", code=302)

if __name__ == '__main__':
   app.run(host= '127.0.0.1', port=5000, debug=True)
  
