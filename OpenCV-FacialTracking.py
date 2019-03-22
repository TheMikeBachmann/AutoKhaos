'''
    File name: OpenCV-FacialTracking.py
    Author: Mike Bachmann
    Date created: 3/22/19
    Date last modified: 3/22/19
    Python Version: 3.6.7
'''

import numpy as np
import cv2
import math

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

frame = cap.read()

#Centerpoint of camera for determining crosshair proximity to target
imgCenter = [320, 240]

while(True):
    
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #Is there a face on screen
    if(type(faces) is np.ndarray):
        #when ready, spin up the motor for X amt of seconds. Send keepalive as long as there is at least one target on screen
        print("Ready")
    else:
        print("Not Ready")

    #Draw boxes around targets
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        faceCenter = (x+w/2, y+h/2)

        #If face is within 100 pixels of center point, fire.
        #TODO: Check if motor is spinning before firing.
        if((math.sqrt( ((imgCenter[0]-faceCenter[0])**2)+((imgCenter[1]-faceCenter[1])**2))) < 100):
            print("FIRE")

    #Not needed, visual for testing unless I decide to mount a viewfinder on the gun.
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

