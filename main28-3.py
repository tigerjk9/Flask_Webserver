from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/map')  # /map에 접속하면 template 폴더의 uni_map.html 파일을 응답합니다.
def map():
    return render_template("uni_map.html")

def main():
    app.run(debug=True,port=80)
    
if __name__== '__main__':
    main()