"""
This module provides emotion detection capabilities using Watson NLP API.
"""
import requests

def emotion_detector(text_to_analyse: str) -> dict:
    """
    Analyzes the sentiment of the provided text and returns emotion scores.

    Args:
        text_to_analyse (str): The text to be analyzed for emotions.

    Returns:
        dict: A dictionary containing emotion scores (anger, disgust, fear, joy, sadness)
              and the dominant_emotion.
    """
    # URL for the Watson NLP Emotion Predict service
    base_url = 'https://sn-watson-emotion.labs.skills.network'
    path = '/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    url = f"{base_url}{path}"

    # Headers for the request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Input JSON for the request
    input_json = {"raw_document": {"text": text_to_analyse}}

    # Handle empty input as per requirements
    if not text_to_analyse.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    try:
        # Sending the POST request to Watson NLP API
        response = requests.post(url, json=input_json, headers=headers, timeout=10)

        # Handling 400 status code
        if response.status_code == 400:
            return {
                "anger": None, "disgust": None, "fear": None,
                "joy": None, "sadness": None, "dominant_emotion": None
            }

        # Parsing JSON response
        formatted_response = response.json()

        # Extracting emotions from response
        if 'emotionPredictions' in formatted_response and formatted_response['emotionPredictions']:
            emotions = formatted_response['emotionPredictions'][0]['emotion']
            dominant_emotion = max(emotions, key=emotions.get)

            return {
                "anger": emotions.get('anger'),
                "disgust": emotions.get('disgust'),
                "fear": emotions.get('fear'),
                "joy": emotions.get('joy'),
                "sadness": emotions.get('sadness'),
                "dominant_emotion": dominant_emotion
            }

    except requests.exceptions.RequestException:
        # Handle exceptions from Watson API
        return {"error": "API connection failed"}

    return {"error": "Unexpected response format from API"}

if __name__ == "__main__":
    # Example usage for terminal testing
    print(emotion_detector("I am so happy that this is working!"))
