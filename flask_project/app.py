from flask import Flask, render_template, request

app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html', ip_address=request.remote_addr)


@app.route('/')
def index():
    ip_address = request.headers.get('X-Real-IP', request.remote_addr)
    return render_template('index.html', ip_address=ip_address)
