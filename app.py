from flask import Flask, render_template, request
from phishing_predictor import load_model, predict_url, get_explanation

app = Flask(__name__)

# Load the model once
model = load_model('phishingdetection.pth')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url']
    result, confidence = predict_url(model, url)
    explanation, suggestion = get_explanation(result, url)
    
    return render_template(
        'index.html',
        url=url,
        result=result,
        confidence=confidence,
        explanation=explanation,
        suggestion=suggestion
    )

if __name__ == '__main__':
    app.run(debug=True)
