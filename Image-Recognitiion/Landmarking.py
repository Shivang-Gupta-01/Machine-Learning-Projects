import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("../../datasets/shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

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

        for point in landmarks.parts():
            cv2.circle(frame, (point.x,point.y),2,(255,0,0),3)  # tthis loops visualy represents all the points on the face





    #print(faces)

    if ret:
        cv2.imshow("My Screen",frame)


    key = cv2.waitKey(1)
    if key==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()



