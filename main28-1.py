from flask import Flask  # flask를 FLASK의 이름으로 불러온다. 

app = Flask(__name__)

@app.route('/')   # 주소로 접속하면 hello를 반환합니다. 즉 보여줍니다. 
def hello():
    return "hello"

def main():     # main 함수 생성하기 
    app.run(debug=True,port=80)   # flask 웹서버를 실행한다. 
    
if __name__== '__main__':   # 코드 실행시 main 함수 실행하기
    main()