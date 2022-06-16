import face_recognition
import cv2
import os
import pickle
import numpy as np

class fr_main:
    def __init__(self):
        self.known_encodings = []
        self.known_names = []
        self.frame_size = 0.25
        self.load_encoding_images()
    

    def load_encoding_images(self):
        print("loading encodings...")
        # load the known faces and embeddings
        data = pickle.loads(open("encodings.pickle", "rb").read())
        # initialize the list of encodings andf names for each face detected
        self.known_encodings = data["encodings"]
        self.known_names = data["names"]
        print(self.known_names)
        
        
       
    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_size, fy=self.frame_size)
        # Find all the faces and face encodings in the current frame of webcam video
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame,model="hog")
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations,model="large")

        face_names = []
        for face_encoding in face_encodings:
            # check if the face is match of the encoded faces
            matches = face_recognition.compare_faces(self.known_encodings, face_encoding)
            name = ""
            if True in matches:
                 first_match_index = matches.index(True)
                 name = self.known_names[first_match_index]
            face_names.append(name)

        # Convert to numpy array to adjust coordinates with frame resizing quickly
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_size
        return face_locations.astype(int), face_names
