from flask import Flask, request, render_template
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer

# Load the saved vectorizer and model
with open(r'C:\Users\susha\OneDrive\Desktop\New folder (2)\vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

with open(r'C:\Users\susha\OneDrive\Desktop\New folder (2)\gradient_boosting_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

def preprocess_url(url):
    """Preprocess the given URL."""
    tokenizer = RegexpTokenizer(r'[A-Za-z]+')
    stemmer = SnowballStemmer("english")

    # Tokenize, stem, and join the tokens
    tokens = tokenizer.tokenize(url)
    stemmed_tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(stemmed_tokens)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        if not url:
            return render_template('index.html', prediction=None, error="Please enter a URL.")

        try:
            # Preprocess the URL
            preprocessed_url = preprocess_url(url)

            # Convert the preprocessed text into vectorized form
            vectorized_url = vectorizer.transform([preprocessed_url])

            # Predict using the loaded model
            prediction = model.predict(vectorized_url)[0]

            # Determine the result
            if prediction == 'bad':
                return render_template('index.html', 
                                       prediction="Dangerous Website! ⚠", 
                                       result_color="red", 
                                       emoji="⚠")
            else:
                return render_template('index.html', 
                                       prediction="Safe Website! ☺", 
                                       result_color="green", 
                                       emoji="☺")
        except Exception as e:
            return render_template('index.html', prediction=None, error=f"An error occurred: {str(e)}")

    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
