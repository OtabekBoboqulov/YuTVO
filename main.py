# Import required libraries
import cv2  # OpenCV for video capture and image processing
import face_recognition as fr  # Face recognition library for encoding and matching faces
import pickle  # For saving/loading face data to/from file
from tkinter import *  # GUI library for creating the name entry dialog
from tkinter import ttk


def recognizer(encodings):
    """
    Creates a GUI dialog to assign names to unknown faces.
    
    Args:
        encodings: List of face encodings for unknown faces detected in the current frame
    """
    global known_encodings, known_names

    def recognize():
        """Callback function that saves entered names and closes the dialog."""
        # Add each entered name and its corresponding encoding to the known lists
        for i in range(len(entries)):
            known_names.append(entries[i].get())
            known_encodings.append(encodings[i])
        root.destroy()

    # Count number of unknown faces to create entries for
    cnt = len(encodings)

    # Create and configure the Tkinter window
    root = Tk()
    root.title(win_name)
    root.geometry(f'+{width+10}+0')  # Position window next to the video feed

    # Create text entry fields for each unknown face
    entries = list()
    for j in range(cnt):
        Label(root, text=f'unknown-{j+1}:').grid(row=j, column=0)
        ent = ttk.Entry(root, width=20)
        ent.grid(row=j, column=1)
        entries.append(ent)

    # Add OK button to submit the names
    btn = ttk.Button(root, text='Ok', command=recognize)
    btn.grid(row=cnt+1, column=1, sticky='e')
    root.mainloop()


# Load existing face data from file
# Try to load previously saved face encodings and names from database file
try:
    with open('db.pkl', 'rb') as file:
        data = pickle.load(file)
        known_encodings = data['encodings']  # List of face encodings
        known_names = data['names']  # Corresponding list of names
except FileNotFoundError:
    # If file doesn't exist, start with empty lists
    known_encodings = []
    known_names = []

# Configure video capture window settings
width = 640  # Frame width in pixels
height = 360  # Frame height in pixels
win_name = 'YuTVO'  # Window title

# Initialize camera with DirectShow backend
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # change camera ID as needed
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)  # Set frame rate to 30 FPS
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))  # Use MJPEG codec
cv2.namedWindow(win_name)
cv2.moveWindow(win_name, 0, 0)  # Position window at top-left corner

# Configure text display settings for face labels
font_face = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (255, 0, 0)  # Blue color in BGR format
font_thickness = 1

# face detection setup (unused alternative method)
# face_mesh = FaceMesh()
# face_divisor = 40

# Main video processing loop
while True:
    # Capture frame from camera
    _, _frame = cam.read()
    frame = cv2.flip(_frame, 1)  # Mirror the frame horizontally
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for face_recognition library

    # Detect faces in the current frame
    unknown_locations = fr.face_locations(frameRGB)  # Get bounding boxes of all faces
    unknown_encodings = fr.face_encodings(frameRGB, unknown_locations)  # Get face encodings

    # Process each detected face
    i = 1  # Counter for unknown faces
    unknowns = list()  # List to store encodings of unrecognized faces
    for location, unknown_encoding in zip(unknown_locations, unknown_encodings):
        # Extract bounding box coordinates (top, right, bottom, left)
        top_left = (location[3], location[0])
        bottom_right = (location[1], location[2])

        # Default label for unrecognized faces
        name = f'unknown-{i}'

        # Draw rectangle around the face
        cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), 1)

        # Compare detected face with known faces
        matches = fr.compare_faces(known_encodings, unknown_encoding)
        if True in matches:
            # Face is recognized - get the corresponding name
            ind = matches.index(True)
            name = known_names[ind]
        else:
            # Face is not recognized - add to unknowns list
            i += 1
            unknowns.append(unknown_encoding)

        # Display the name label above the face
        cv2.putText(frame, name, top_left, font_face, font_scale, font_color, font_thickness)

    # Display the frame with annotations
    cv2.imshow(win_name, frame)

    # Handle keyboard input
    key = cv2.waitKey(1) & 0xff
    if key == ord('q'):
        # Quit the application
        break
    elif key == ord('o'):
        # Open dialog to assign names to unknown faces
        recognizer(unknowns)

# Cleanup - release camera and close windows
cam.release()
cv2.destroyAllWindows()

# Save updated face data to file
data = {
    'encodings': known_encodings,
    'names': known_names
}

with open('db.pkl', 'wb') as file:
    pickle.dump(data, file)