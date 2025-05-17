import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    # Define test cases mapping input statements to expected dominant emotions
    TEST_CASES = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear"),
    ]

    def test_emotion_scores_and_dominant(self):
        """
        Test that emotion_detector returns all five emotion scores between 0 and 1,
        and that the dominant_emotion matches the expected value for each case.
        """
        for text, expected in self.TEST_CASES:
            with self.subTest(text=text, expected=expected):
                result = emotion_detector(text)

                # Ensure all keys exist
                for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']:
                    self.assertIn(key, result, f"Missing key: {key}")

                # Ensure scores are floats within [0.0, 1.0]
                for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness']:
                    score = result[emotion]
                    self.assertIsInstance(score, float, f"Score for {emotion} is not float")
                    self.assertGreaterEqual(score, 0.0, f"Score for {emotion} is less than 0.0")
                    self.assertLessEqual(score, 1.0, f"Score for {emotion} is greater than 1.0")

                # Check dominant emotion
                self.assertEqual(result['dominant_emotion'], expected,
                                 f"Expected dominant {expected}, got {result['dominant_emotion']}")

if __name__ == '__main__':
    unittest.main()
