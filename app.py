from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reserve", methods=["POST"])
def reserve():
    name = request.form["name"]
    phone = request.form["phone"]
    date = request.form["date"]
    time = request.form["time"]
    people = request.form["people"]
    print(f"📥 예약 수신: {name}, {phone}, {date}, {time}, {people}", flush=True)
    return f"{name}님의 예약이 완료되었습니다!"

# 로컬 테스트용 실행
if __name__ == "__main__":
    app.run(debug=True)

