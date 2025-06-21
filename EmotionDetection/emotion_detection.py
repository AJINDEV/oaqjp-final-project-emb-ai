import requests
import json

def emotion_detector(text_to_analyze):
    # URL for the Watson NLP Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers required for the API call
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Input JSON payload structured for the API
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Make the POST request to the API
    response = requests.post(url, json = myobj, headers=header)
    
    # Check the status code of the response
    if response.status_code == 400:
        # If the status code is 400, it means an invalid request (e.g., blank text)
        # Return a dictionary with None values as required
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # If the request was successful, proceed with formatting the output
    formatted_response = json.loads(response.text)
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion
    
    return emotion_scores