"""
This is a Flask web application that provides an interface for
emotion detection. It serves a main page and an API endpoint
to process text and return the detected emotions.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Handles the emotion detection logic.
    Retrieves text from the request arguments, passes it to the
    emotion_detector function, and formats a response string.
    If the input is invalid, it returns an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    dominant_emotion = response.pop('dominant_emotion')
    output_string = ", ".join([f"'{k}': {v}" for k, v in response.items()])

    return (
        f"For the given statement, the system response is {output_string}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main HTML page of the application.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    