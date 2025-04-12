import cv2
import numpy as np
import face_recognition
from sklearn.preprocessing import MinMaxScaler
import time

class FaceRater:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.scaler = MinMaxScaler(feature_range=(1, 10))
        
    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces

    def get_face_features(self, frame, face):
        x, y, w, h = face
        face_img = frame[y:y+h, x:x+w]
        
        # Get face landmarks
        face_landmarks = face_recognition.face_landmarks(face_img)
        if not face_landmarks:
            return None
            
        # Calculate symmetry score
        left_eye = np.mean(face_landmarks[0]['left_eye'], axis=0)
        right_eye = np.mean(face_landmarks[0]['right_eye'], axis=0)
        nose_tip = face_landmarks[0]['nose_tip'][0]
        
        # Calculate distances
        left_eye_nose = np.linalg.norm(left_eye - nose_tip)
        right_eye_nose = np.linalg.norm(right_eye - nose_tip)
        
        # Calculate symmetry score (1-10)
        symmetry_score = 10 * (1 - abs(left_eye_nose - right_eye_nose) / max(left_eye_nose, right_eye_nose))
        
        return symmetry_score

    def rate_face(self, frame, face):
        features = self.get_face_features(frame, face)
        if features is None:
            return 0
            
        # Combine features into a final score
        final_score = features
        return round(final_score, 1)

    def process_frame(self, frame):
        faces = self.detect_faces(frame)
        
        for (x, y, w, h) in faces:
            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # Rate the face
            score = self.rate_face(frame, (x, y, w, h))
            
            # Display score
            cv2.putText(frame, f'Score: {score}', (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        return frame

def main():
    # Initialize the face rater
    rater = FaceRater()
    
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    print("Starting face rating application...")
    print("Press 'q' to quit")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Process the frame
        processed_frame = rater.process_frame(frame)
        
        # Display the frame
        cv2.imshow('Face Rating', processed_frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 