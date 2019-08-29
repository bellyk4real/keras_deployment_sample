from flask import Flask
from flask import request

# create the Flask app
app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1234)