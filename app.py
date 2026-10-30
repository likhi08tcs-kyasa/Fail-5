import sqlite3
from flask import Flask, request

app = Flask(__name__)
API_KEY = "sk-test-1234567890abcdef"  # hardcoded secret


def get_user(username):
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (username TEXT)")
    cur.execute("INSERT INTO users (username) VALUES (?)", ("test",))
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cur.execute(query)
    result = cur.fetchall()
    conn.close()
    return result


@app.route("/user")
def user():
    return str(get_user(request.args.get("username", "")))


@app.route("/calc")
def calc():
    return str(eval(request.args.get("expr", "1")))  # code injection


if __name__ == "__main__":
    app.run(debug=True)
