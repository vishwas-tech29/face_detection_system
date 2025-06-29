import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
from playsound import playsound
from utils.logger import log_detection

# === Load known faces ===
print("[INFO] Loading known faces...")
known_face_encodings = []
known_face_names = []

known_faces_dir = 'known_faces'
for filename in os.listdir(known_faces_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        path = os.path.join(known_faces_dir, filename)
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_face_encodings.append(encodings[0])
            known_face_names.append(os.path.splitext(filename)[0])

# === Start video capture ===
print("[INFO] Starting camera...")
video = cv2.VideoCapture(0)

detected = False

try:
    while not detected:
        ret, frame = video.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            if True in matches:
                match_index = np.argmin(face_recognition.face_distance(known_face_encodings, face_encoding))
                name = known_face_names[match_index]

                # Crop the detected face
                top, right, bottom, left = face_location
                face_crop = frame[top:bottom, left:right]

                # Generate filename and save image
                timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                image_name = f"{name}_{timestamp}.jpg"
                image_path = os.path.join("logs", "images", image_name)
                cv2.imwrite(image_path, face_crop)

                # Log detection
                log_detection(name, timestamp, image_name)

                # Play sound
                playsound("assets/detected.mp3")

                # Show frame briefly (optional)
                cv2.imshow("Face Detection", frame)
                cv2.waitKey(1000)  # Display for 1 second
                detected = True
                break

        cv2.imshow("Face Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\n[INFO] Stopped by user.")

finally:
    video.release()
    cv2.destroyAllWindows()
    print("[INFO] Program exited cleanly.")
