
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def automation():
    return render_template("automation.html",
                           )

@app.route('/automated', methods = ['post', 'get'])
def automated():
    tubelight = request.form['geto']
    from av import iot_led as il
    tubelight = il.run(tubelight)
    return render_template("automation.html",
                            tubelight=int(tubelight),
                           )
@app.route('/automating')
def automating():
    return render_template("index.html",
                           )



if __name__ == "__main__":
    app.run(debug=True)
    