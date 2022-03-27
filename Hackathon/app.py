from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "hello! this is the main page <h1>hello<h1>"

@app.route('/automation')
def automation():
    return render_template("automation.html",
                           )

@app.route('/automated', methods = ['post', 'get'])
def automated():
    led_on = request.form['geto']
    from av import iot_led as il
    led_on = il.run(led_on)
    return render_template("automation.html",
                            led_on=int(led_on),
                           )

if __name__ == "__main__":
    app.run(debug=True)