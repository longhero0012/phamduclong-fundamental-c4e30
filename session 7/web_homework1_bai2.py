from flask import Flask
app = Flask(__name__)


@app.route('/user/<username')
def index(nguoi_dung ):
  Users = {
  	“huy” = {
			“name” : “Nguyen Quang Huy”,
			“age” : 29
       },
    “tuananh” =
     {
			“name” : “Huynh Tuan Anh”,
			“age” : 22
       }
} 
for i in users :
  if nguoi_dung in users :
    return (Users[nguoi_dung])
  else :
    return ("không tồn tại thông tin ")


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 