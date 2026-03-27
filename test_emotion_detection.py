import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy
        result_1 = emotion_detector("I am glad this happened")
        if result_1.get("dominant_emotion"):
            self.assertEqual(result_1["dominant_emotion"], "joy")
        
        # Test case for anger
        result_2 = emotion_detector("I am really mad about this")
        if result_2.get("dominant_emotion"):
            self.assertEqual(result_2["dominant_emotion"], "anger")
        
        # Test case for disgust
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        if result_3.get("dominant_emotion"):
            self.assertEqual(result_3["dominant_emotion"], "disgust")
        
        # Test case for sadness
        result_4 = emotion_detector("I am so sad about this")
        if result_4.get("dominant_emotion"):
            self.assertEqual(result_4["dominant_emotion"], "sadness")
        
        # Test case for fear
        result_5 = emotion_detector("I am really afraid that this will happen")
        if result_5.get("dominant_emotion"):
            self.assertEqual(result_5["dominant_emotion"], "fear")

    def test_empty_input(self):
        # Test case for empty input
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])

if __name__ == "__main__":
    unittest.main()
