import cv2
import face_recognition

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not video.isOpened():
    print("[ERROR] Could not open webcam.")
    exit()

print("[INFO] Webcam started. Press 'q' to quit.")

while True:
    ret, frame = video.read()
    if not ret:
        print("[ERROR] Can't receive frame.")
        break

    rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB
    face_locations = face_recognition.face_locations(rgb_frame)

    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
# Note: This code is a simplified version for testing webcam functionality.
# It does not include face recognition or logging features.