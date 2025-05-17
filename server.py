"""Flask app for emotion detection with PEP8-compliant server code."""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

APP = Flask(__name__)


@APP.route("/", methods=["GET"])
def index():
    """Render the main index page."""
    return render_template("index.html")


@APP.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Retrieve text from request arguments, analyze emotions,
    and return JSON response or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    # Pre-empt blank or whitespace-only input
    if not text_to_analyze:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    result = emotion_detector(text_to_analyze)

    # Handle service-level errors
    if result.get("dominant_emotion") is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    message = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"scores": result, "message": message})


def main():
    """Run the Flask development server."""
    APP.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
