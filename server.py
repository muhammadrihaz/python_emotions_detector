"""
Flask server for Emotion Detector AI.
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotion")
def emot_detector():
    """
    Analyzes the text provided in the query parameters for emotions.
    """
    text_to_analyze = request.args.get('text')

    # Use the emotion_detector function to analyze the text
    response = emotion_detector(text_to_analyze)

    # Extract the emotion scores and dominant_emotion from the response
    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')
    dominant_emotion = response.get('dominant_emotion')

    # Check if the dominant_emotion is None (invalid text)
    if dominant_emotion is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    # Return the formatted response
    return jsonify({
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    })

@app.route("/")
def render_index_page():
    """
    Renders the main application page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
