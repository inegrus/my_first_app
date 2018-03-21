from flask import Flask, render_template

app = Flask("MyApp")


@app.route("/")
def hello():
    return "Hello!"


@app.route("/idontexist")
def idontexist():
    return "I do exist now!"


@app.route("/ioanaravar")
def myname():
    return "I really like ice-cream!"


app.run(debug=True)
