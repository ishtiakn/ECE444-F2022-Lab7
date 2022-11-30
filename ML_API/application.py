# This is the ML API.
# It accepts requests with text and predicts if that text is fake news.

from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)

###### Model Loading ######
loaded_model = None
with open('models/basic_classifier.pkl', 'rb') as fid:
    loaded_model = pickle.load(fid)
    
vectorizer = None
with open('models/count_vectorizer.pkl', 'rb') as vd:
    vectorizer = pickle.load(vd)
    
###### Server ######
@application.route('/ML_API', methods=['POST'])
def predict():
        try:
            data = request.get_json(force=True)
            prediction = loaded_model.predict(vectorizer.transform([str(data)]))[0]
            if str(prediction) == 'FAKE':
                return jsonify(1)
            else:
                return jsonify(0)  
            
        except Exception as e:
            return("ERROR: ", e)

if __name__ == '__main__':
    application.run()
    