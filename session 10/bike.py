from flask import Flask, render_template, request
from db1 import get_all,add_bike
app = Flask(__name__)


@app.route('/new_bike')
def get_bike():
    return render_template('bike.html')

@app.route('/new_bike', methods=["POST"])
def post_bike():
  name = request.form.get('name')
  dayly =request.form.get('dayily_fee')
  image = repuest.form.get('image')
  year = request.form.get('year')
  return render_template('bike.html')
print (get_all())
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 