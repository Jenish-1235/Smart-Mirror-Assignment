# Smart Mirror and Meta Quest Integration Project

## Overview

This project comprises three main components:

1.   **Face Emotion Detection Model:** A python project that uses machine learning model from fer to detect faces and emotion and generates compliments based on emotions and speaks it. [Link to Repository](https://github.com/Jenish-1235/Smart-Mirror-Assignment)
2.   **StyleUp Android App Repository:** A mobile application that uses machine learning (ML) models to detect and mark body points in real-time for fashion and style recommendations. [Link to Repository](https://github.com/Jenish-1235/StyleUp)
3.  **MetaQuest and Unity Integration Repository:** An AR/VR project aimed at integrating smart mirror features into Meta Quest using Unity. This repository supports virtual try-ons and 3D experiences. [Link to Repository](https://github.com/Jenish-1235/smart-mirror-assignment-metaquest)
    

## Features

### Face Emotion Detection Model
-  **Face Detection:** Detection of faces in realtime video feed.
-  **Emotion Analysis:** Realtime Emotion and Sentiment detection and compliment generation.
-  **Text-to-Speech:** Converts text message of detected emotion and compliment to speech.

### StyleUp Android Application (Under Development)

-   **Body Pose Detection:** Leverages advanced ML models to detect body points for analyzing posture and movement.
-   **Real-Time Detection:** Processes live camera input to detect and mark body points dynamically.
-   **Style Recommendations:** Provides fashion suggestions based on detected posture and body data.
-   **Easy Integration:** Designed to integrate seamlessly with other AR/VR components of the smart mirror project.

### MetaQuest and Unity Integration (Under Development)

-   **AR/VR Features:** Supports virtual try-on of clothes and accessories in an immersive environment.
-   **Unity Integration:** Uses Unity to build and render 3D models and integrate the smart mirror’s functionalities.
-   **Cross-Platform Compatibility:** Designed for Meta Quest, with potential extensions for Apple Vision Pro and similar AR/VR headsets.
-   **Smart Mirror Features:** Includes emotion detection, voice output, and personalized fashion suggestions.

## Setup Instructions

### Python - Face Detection 

1. **Clone the Repository:**
   
    ```bash
    git clone https://github.com/Jenish-1235/Smart-Mirror-Assignment/
    
    ```
2. **Install required packages using:**
   ```bash
   pip install -r requirements.txt
   ```
3. Run main.py

### StyleUp Android Application

1.  **Clone the Repository:**
    
    ```bash
    git clone https://github.com/Jenish-1235/StyleUp.git
    
    ```
    
2.  **Install Dependencies:**
    
    -   Use Android Studio to open the project.
    -   Sync the Gradle files to install all required dependencies.
3.  **Run the Application:**
    
    -   Connect an Android device or use an emulator.
    -   Build and run the project.
4.  **Configure ML Model:**
    
    -   Place your ML model in the `assets` directory.
    -   Update the configuration in the code to point to the correct model file.

### MetaQuest and Unity Integration

1.  **Clone the Repository:**
    
    ```bash
    git clone https://github.com/Jenish-1235/smart-mirror-assignment-metaquest.git
    
    ```
    
2.  **Install Unity:**
    
    -   Download and install Unity (ensure compatibility with the Unity version used in the project).
    -   Install the necessary Unity packages (e.g., AR Foundation, Oculus Integration).
3.  **Open the Project:**
    
    -   Open the repository in Unity Hub.
    -   Allow Unity to import all assets and dependencies.
4.  **Run on Meta Quest:**
    
    -   Connect your Meta Quest device.
    -   Build and deploy the project to the headset.

## Project Architecture

-   **ML Model:** FER Model for face and emotion detection.
-   **Text-to-Speech:** Pyttsx3 for text to speak conversion of compliments and detected emotion.

### StyleUp Android App

-   **ML Model:** Firebase MLKit (TFLite) model for pose detection.
-   **Camera Integration:** Utilizes Android CameraX API for real-time video feed.
-   **UI/UX:** Material Design principles for intuitive navigation.

### MetaQuest and Unity Project

-   **Unity:** Main engine for rendering 3D models and AR/VR interactions.
-   **Oculus Integration:** SDK for seamless Meta Quest integration.
-   **Voice and Emotion Analysis:** Uses additional APIs for voice-based suggestions and emotion detection.

## Future Enhancements

-   Extend support for other AR/VR devices such as Apple Vision Pro.
-   Incorporate advanced AI models for style and trend predictions.
-   Improve UI/UX for both Android and AR/VR components.
-   Enable synchronization between Android app and AR/VR projects for a unified experience.

## Contribution Guidelines

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes and submit a pull request.
4.  Follow the project’s code of conduct.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or collaborations, contact:

-   Jenish [Email](mailto:jenishtogadiya549@gmail.com)

## Links
-   [Face-Detection-Model](https://github.com/Jenish-1235/Smart-Mirror-Assignment)
-   [StyleUp Repository](https://github.com/Jenish-1235/StyleUp)
-   [MetaQuest Integration Repository](https://github.com/Jenish-1235/smart-mirror-assignment-metaquest)
