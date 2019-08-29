from flask import Flask
from flask import request
from keras.preprocessing import sequence
from keras.models import load_model
from keras.preprocessing.text import text_to_word_sequence
from keras.datasets import imdb
import numpy as np

# maximum words in each sentence
maxlen = 10
# get the word index from imdb dataset
word_index = imdb.get_word_index()
# load the Model from file
nlp_model = load_model('model/imdb_nlp.h5')
# method that does the prediction – we will call this later
def predict_sentiment(my_test):
    # tokenize the sentence
    word_sequence = text_to_word_sequence(my_test)
    # create a blank sequence of integers
    int_sequence = []
    # for each word in the sentence
    for w in word_sequence:
        # get the integer from vocabulary and add to list
        int_sequence.append(word_index[w])
        # pad the sequence of numbers to input size expected by model
        sent_test = sequence.pad_sequences([int_sequence],
            maxlen=maxlen)
        # make a prediction using our Model
        y_pred = nlp_model.predict(sent_test)
        # return a predicted sentiment real value between 0 and 1
        return y_pred[0][0]


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