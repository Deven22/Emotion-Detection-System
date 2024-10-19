from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model and vectorizer
model = joblib.load('emotion_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Emotion to icon mapping
emotion_to_icon = {
    'happiness': 'static/icons/happy.png',
    'sadness': 'static/icons/sad.png',
    'angry': 'static/icons/angry.png',
    'surprise': 'static/icons/surprised.png',
    'hate': 'static/icons/hate.png',
    'neutral': 'static/icons/neutral.png',
    'worry': 'static/icons/worry.png',
    'love': 'static/icons/love.png',
    'relief': 'static/icons/relieved.png',
    'fun': 'static/icons/fun.png',
          
}

# Home route to display the frontend
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle emotion detection
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data['text']
    
    # Preprocess text and predict emotion
    text_vector = vectorizer.transform([text]).toarray()
    prediction = model.predict(text_vector)[0]
    
    # Get the corresponding icon for the predicted emotion
    icon_url = emotion_to_icon.get(prediction, 'static/icons/neutral.png')  # Default icon for unknown emotions
    
    # Return the prediction and icon URL
    return jsonify({'emotion': prediction, 'icon_url': icon_url})

if __name__ == '__main__':
    app.run(debug=True)
