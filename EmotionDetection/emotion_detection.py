import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request

    response = requests.post(url, json=myobj, headers=header)
    response.raise_for_status()
    data = response.json()
    emotions = data["emotionPredictions"][0]["emotion"]
    dominant = max(emotions, key=emotions.get)
    return {
        'anger':    emotions.get('anger',    0.0),
        'disgust':  emotions.get('disgust',  0.0),
        'fear':     emotions.get('fear',     0.0),
        'joy':      emotions.get('joy',      0.0),
        'sadness':  emotions.get('sadness',  0.0),
        'dominant_emotion': dominant
    }