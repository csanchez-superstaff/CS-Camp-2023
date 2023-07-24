#install python and vs code based on your mac or windows computer. you can follow youtube tutorial to do that. it is pretty easy and should not take more than 10 minutes. 


import cv2 #type < pip install opencv-python > on terminal to download the library
import numpy as np #type < pip install numpy > on terminal to download the library
import pyautogui #type < pip install pyautogui > on terminal to download the library
import mediapipe as mp #type < pip install mediapipe > on terminal to download the library

# Constants for the circle radius and thickness
circle_radius = 10
circle_thickness = 2

# Variables to store the current position of the mouse
mouse_position = (0, 0)

# Function to move the mouse cursor
def move_mouse():
    global mouse_position
    screen_width, screen_height = pyautogui.size()
    x, y = mouse_position
    # Normalize the x, y values based on the screen size
    x_normalized = x / cap_width
    y_normalized = y / cap_height
    # Move the mouse cursor
    pyautogui.moveTo(int(x_normalized * screen_width), int(y_normalized * screen_height))

# Function to open a file at the current mouse position
def open_file():
    global mouse_position
    x, y = mouse_position
    # Simulate a mouse click at the current position
    pyautogui.click(x, y)

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

# Get the width and height of the capture frame
cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Initialize the hand tracking module from Mediapipe
mp_hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)

# Set the initial mouse position at the center of the frame
mouse_position = (cap_width // 2, cap_height // 2)

# Create a window to display the video feed
cv2.namedWindow('Webcam')

while True:
    # Read a frame from the video feed
    ret, frame = cap.read()

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB and pass it to the hand tracking module
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_hands.process(frame_rgb)

    # Check if any hands are detected
    if results.multi_hand_landmarks:
        # Get the landmark positions of the first detected hand
        hand_landmarks = results.multi_hand_landmarks[0]
        for landmark in hand_landmarks.landmark:
            # Convert normalized landmark coordinates to pixel values
            x = int(landmark.x * cap_width)
            y = int(landmark.y * cap_height)
            if landmark.HasField('visibility') and landmark.visibility < 0.1:
                # If the landmark is not visible, skip it
                continue
            # Update the mouse position
            mouse_position = (x, y)
            # Draw a circle at the current mouse position
            cv2.circle(frame, mouse_position, circle_radius, (0, 0, 255), circle_thickness)

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Check for the 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Move the mouse cursor based on the finger position
    move_mouse()

    # Check if the finger is pressed to open a file
    if cv2.waitKey(1) & 0xFF == ord('f'):
        open_file()

# Release the video capture and destroy the windows
cap.release()
cv2.destroyAllWindows()
