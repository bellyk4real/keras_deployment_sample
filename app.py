from flask import Flask
from flask import request

# create the Flask app
app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, World!'

# default HTML to show at first when no input is sent
htmlDefault = '<h4>Simple Python NLP demo</h4><form><textarea rows=10cols=100 name=\'text_input\'></textarea><br><input type=submit></form>'

# build a route or HTTP endpoint
# this route will read text parameter and analyze it
@app.route('/process')
def process():
    # get the HTTP parameter by name 'text_input'
    in_text = request.args.get('text_input')
    # if input is provided process else show default page
    if in_text is not None:
        # just show
        return 'You typed: <b>%s</b>'%(in_text)
    else:
        return htmlDefault

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1234)