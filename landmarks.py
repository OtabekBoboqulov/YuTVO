import mediapipe as mp
import cv2


class FaceMesh:
    def __init__(self):
        self.results = None
        self.face_mesh = mp.solutions.face_detection.FaceDetection()
        self.drawer = mp.solutions.drawing_utils

    def marks(self, frame, width=640, height=1280):
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.face_mesh.process(frameRGB)
        faces = list()
        if self.results.detections is not None:
            for face_landmarks in self.results.detections:
                box = face_landmarks.location_data.relative_bounding_box
                top_left = (int(box.xmin * width), int(box.ymin * height))
                bottom_right = (int((box.xmin + box.width) * width), int((box.ymin + box.height) * height))
                faces.append((top_left, bottom_right))
        return faces

    def draw(self, frame):
        if self.results.detections is not None:
            for face in self.results.detections:
                self.drawer.draw_detection(frame, face)
