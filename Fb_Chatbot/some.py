from flask import Flask,request
app = Flask("chacha")
@app.route("/home/")
def Hello():
    return str(request.args)
app.run()