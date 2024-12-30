compliments = {
    "happy": "Your smile lights up the room!",
    "neutral": "Your presence is calm and confident!",
    "sad": "You’ve got this, keep going!",
}

def get_compliment(emotion):
    return compliments.get(emotion, "You're amazing!")
