from fer import FER

# Emotion detector initialization
detector = FER(mtcnn=True)

def analyze_emotion(image):
    emotion, score = detector.top_emotion(image)
    return emotion
