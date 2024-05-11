import cv2
# Load the Haar cascade XML file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    ret, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)# Convert the frame to grayscale

    faces = face_cascade.detectMultiScale(gray, 1.3,5) # Detect faces in the grayscale frame
    # Draw a green bounding box around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Display the frame with the bounding boxes
    cv2.imshow('Face Detection', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):# Break the loop if the 'q' key is pressed
        break
cap.release()
cv2.destroyAllWindows()
