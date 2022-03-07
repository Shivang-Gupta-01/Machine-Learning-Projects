import numpy as np
import cv2
from sklearn.neighbors import KNeighborsClassifier
import dlib

data = np.load("face_mood.npy")
print(data.shape,data.dtype)

X = data[:,1:].astype(np.uint8)  # or int
y = data[:,0]

model = KNeighborsClassifier()
model.fit(X,y)

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("../../datasets/shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray,face)
        nose = landmarks.parts()[27]
        expression = np.array([[point.x-face.left(),point.y-face.top()] for point in  landmarks.parts()[17:] ])

        print(model.predict(expression.flatten()))

    if ret:
        cv2.imshow("My Screen",frame)


    key = cv2.waitKey(1)

    if key==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()



