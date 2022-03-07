import cv2
import dlib
import numpy as np
import os

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("../../datasets/shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

mood = input("Enter your expression/mood : ")

frames =[]
outputs =[]

while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:

        landmarks = predictor(gray,face)
        #print(lanmarks.parts())           # shows all the values for each feature on the shape
        nose = landmarks.parts()[27]       # this only captures the nose coordinates Note: The value of nose is 28 in documentation since they start from 1, since we suse 0 bbased indexing, we will have to use 27
        #print(nose.x,nose.y)
        #cv2.circle(frame, (nose.x, nose.y), 2, (255, 0, 0), 3)

        # lip_up =  landmarks.parts()[62].y
        # lip_down =  landmarks.parts()[66].y
        #
        # if lip_down -lip_up > 5:
        #     print("Mouth Open")
        # else:
        #     print("Mouth Close")

        #for point in landmarks.parts():
        #    cv2.circle(frame, (point.x,point.y),2,(255,0,0),3)  # tthis loops visualy represents all the points on the face


        expression = np.array([[point.x-face.left(),point.y-face.top()] for point in  landmarks.parts()[17:] ])
        #print(expression.flatten())



      #  for point in landmarks.parts()[48:]:
       #     cv2.circle(frame, (point.x, point.y), 2, (255, 0, 0), 3)
            #print(faces)

    if ret:
        cv2.imshow("My Screen",frame)


    key = cv2.waitKey(1)
    if key==ord("q"):
        break
    elif key==ord("c"):
        frames.append(expression.flatten())
        outputs.append([mood])

X = np.array(frame)
y = np.array(outputs)

data = np.hstack([y,X])

#print(data.shape)
f_name = "face_mood.npy"

if os.path.exists(f_name):
    old = np.load(f_name)
    data = np.vstack([old,data])

np.save(f_name,data)


cap.release()
cv2.destroyAllWindows()



