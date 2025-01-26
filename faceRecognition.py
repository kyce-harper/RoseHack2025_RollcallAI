import cv2
import numpy as np
import os
# from flask import Flask, Response, request, jsonify
# from flask_cors import CORS
from cameraCapture import cameraCap

# app = Flask(__name__)
# CORS(app)



def scan():
    capture = cv2.VideoCapture(0)
    faceCap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("Trainer.yml")
    timer = 0
    while True:
        ret, frame = capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converts the image (video-captured image) into grayscale
        #1.3 (2nd parameter) is the scale factor. You must change the size of the image so that haar-cascade can compare it to. the scale factor tells how much to shrink the image to
        # next paramter (5) is the min_neighbor. it's the parameter that teels haar-cascade how many "neighbors" of potential faces to retain it
        
        faces = faceCap.detectMultiScale(gray, 1.4, 6) #returns the position of all the faces that is detected
        # x,y,w,h are the dimensions of the rectangle that are gonna be drawn around a face
        
        for (x,y,w,h) in faces:
            serial, conf = recognizer.predict(gray[y:y+h, x:x+w])
            if conf < 45:
                with open("names.txt", "r") as file:
                    for i in range(0, serial - 1):
                        file.readline()
                    name = file.readline()
                capture.release()
                cv2.destroyAllWindows()
                #return {"Serial": serial, "Name": name, "status":"recognized"} 
            else:
                print(timer)
                timer += 1
                if timer > 20:
                    capture.release()
                    cv2.destroyAllWindows()
                    cameraCap()
                    #return {"status":"memorized yo face lol"}
            
if os.stat("Trainer.yml").st_size == 0:
    cameraCap()
else:
    scan()
    
    
# @app.route('/save-name', methods=['POST'])
# def saveName():
#     data = request.get_json()
#     if not data:
#             return jsonify({"error": "No JSON data received"}), 400
#     name = data.get('text1')
#     #schedule = data.get('text2')
    
#     try:
#         with open("names.txt", "a") as file:
#             file.write(name + "\n")
#         return jsonify({"message": "Name saved successfully!"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
# if __name__ == "__main__":
#     app.run(debug=True)
#print(test())
