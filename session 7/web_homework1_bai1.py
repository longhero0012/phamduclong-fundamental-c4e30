from flask import Flask, render_template
app = Flask(__name__)
  
@app.route('/bmi/cannang/chieucao')
def BMI(cannang,chieucao):
  cannang = int (a)
  chieucao = int (b) 
  bmi = a/(b*b)
  if bmi < 16 :
    return ("thiếu cân nặng")
  elif 16 <= bmi <18.5 :
    return ("thiếu cân")
  elif 18.5 <= bmi <25:
    return ("bình thường ")
  elif 25 <= bmi < 30:
    return ("thừa cân ")
  else :
    return ("béo phì ")   
  
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)