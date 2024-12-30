import cv2
from face_detection import detect_faces
from emotion_analysis import analyze_emotion
from compliment_generator import get_compliment
from visualisation import annotate_image
from text_to_speech import speak_compliment

def process_image(image_path):
    image = cv2.imread(image_path)
    faces = detect_faces(image)
    emotion = analyze_emotion(image)
    compliment = get_compliment(emotion)

    # Optionally speak the compliment
    speak_compliment(compliment)
    
    # Annotate and display the result
    annotated_image = annotate_image(image, faces, emotion, compliment)
    cv2.imshow("Smart Mirror", annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def real_time_feed():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        faces = detect_faces(frame)
        emotion = analyze_emotion(frame)
        compliment = get_compliment(emotion)
        frame = annotate_image(frame, faces, emotion, compliment)
        cv2.imshow('Smart Mirror', frame)

        # Optional: Speak the compliment
        speak_compliment(compliment)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    choice = input("Enter '1' for image mode or '2' for real-time mode: ")
    if choice == '1':
        image_path = input("Enter the image path: ")
        process_image(image_path)
    elif choice == '2':
        real_time_feed()
    else:
        print("Invalid choice. Exiting...")
