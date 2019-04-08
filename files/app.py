from flask import Flask, render_template, request
from mysql import ConnectDB
import json

with open("/tmp/credentials.json", "r") as f:
    credentials = json.load(f)
x = ConnectDB()
app = Flask(__name__)
lista = []


@app.route('/')
def student():
    queryall = x.queryAll(credentials)
    print(queryall)
    return render_template('index.html', student=queryall)


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form.to_dict()
    status = x.CheckUser(result, credentials)
    if len(result['name']) < 1:
            status = {
             "status": "Name cannot be empty!!!"
            }
            return render_template("result.html", result=status), 401

    if status['status'] is not "Success":
        return render_template("result.html", result=status), 401
    return render_template("result.html", result=status)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
