import cv2

def annotate_image(image, faces, emotion, compliment):
    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Display detected emotion
        cv2.putText(image, f"Emotion: {emotion}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        
        # Display compliment
        cv2.putText(image, compliment, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    return image
