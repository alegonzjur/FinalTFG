from flask import Flask 

app = Flask(__name__)

@app.route('/route_name')
def home():
    pass

if __name__ == '__main__':
    app.run('localhost',4499)