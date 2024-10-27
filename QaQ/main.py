import cv2
import random
import time
from plyer import notification
import pygame

# Load the pre-trained Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect faces in a frame from webcam
def detect_faces(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # If there is a face detected and it's been more than 30 seconds since the last launch
        if time.time() - detect_faces.last_launch_time > 5:
            # Play an MP3 file
            pygame.mixer.init()
            pygame.mixer.music.load("tmpusovvyfy.wav")
            pygame.mixer.music.play()
            # Show a popup notification
            notification.notify(
                title="Face Detected",
                message="A face has been detected!",
                app_name="Face Detection",
                timeout=10
            )
            detect_faces.last_launch_time = time.time()  # Update last launch time
    # Display the frame with detected faces
    cv2.imshow('Face Detection', frame)

# Initialize last launch time
detect_faces.last_launch_time = 0

# Main function
def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)
    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    # Loop to continuously capture frames from the webcam
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        # Detect faces in the frame
        detect_faces(frame)
        # Check for the 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
