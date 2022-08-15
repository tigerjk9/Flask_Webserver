from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/1')  # /1에 접속하였을 때 1page ok를 출력합니다.
def test1page():
    return "1page ok"

@app.route('/2')  # /2에 접속하였을 때 2page ok를 출력합니다.
def test2page():
    return "2page ok"

def main():
    app.run(debug=True,port=80)
    
if __name__== '__main__':
    main()