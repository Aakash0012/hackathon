
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def auto():
    return render_template("auto.html",
                           )

@app.route('/automated', methods = ['post', 'get'])
def automated():
    fan = request.form['geto']
    from av import iot_led as il
    fan = il.run(fan)
    return render_template("auto.html",
                            fan=int(fan),
                           )

if __name__ == "__main__":
    app.run(debug=True)
    