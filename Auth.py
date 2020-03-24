import cv2
from align_custom import AlignCustom
from face_feature import FaceFeature
from mtcnn_detect import MTCNNDetect
from tf_graph import FaceRecGraph
# import openpyxl as xl
# import datetime
# import time
import argparse
import sys
import json
import numpy as np
import os 
# from auth1 import every
# import tkinter as tk
# from tkinter import *
# from PIL import ImageTk,Image

# def quit(*args):
#     root.destroy()

# root = Tk()
# root.attributes("-fullscreen", True)
# root.configure(background='black')
# root.bind("<Escape>", quit)
# root.bind("x", quit)

# def ok():
#     global Home
#     root.withdraw()
#     Home = Toplevel()
#     Home.title("FaceCam")
#     Home.configure(background='black')
#     Home.bind("<Escape>", quit)
#     Home.bind("x", quit)
#     Home.attributes("-fullscreen", True)
#     lbl_home=Button(Home, text="Authentication Successful!!", bd=20, bg="black", fg="green", 
#                     font=('times new roman', 20),relief=RIDGE).pack(fill=BOTH, expand=1)
#     # btn_back = Button(Home, text='Back', command=Back).pack(pady=20)

def main(args):
    mode = args.mode
    if(mode == "camera"):
        auth()

def auth():
	names = json.load(open("names.txt"))
	print("[INFO] camera sensor warming up...")
	vs = cv2.VideoCapture(0);
	while True:
		_,frame = vs.read();
		# u can certainly add a roi here but for the sake of a demo i'll just leave it as simple as this
		rects, landmarks = face_detect.detect_face(frame, 80);#min face size is set to 80x80
		aligns = []
		positions = []



		for (i, rect) in enumerate(rects):
		    aligned_face, face_pos = aligner.align(160,frame,landmarks[i])
		    if len(aligned_face) == 160 and len(aligned_face[0]) == 160:
		        aligns.append(aligned_face)
		        positions.append(face_pos)
		    else: 
		        print("Align face failed") #log        
		if(len(aligns) > 0):
		    features_arr = extract_feature.get_features(aligns)
		    recog_data = findPeople(features_arr,positions);
		    for (i,rect) in enumerate(rects):
		        cv2.rectangle(frame,(rect[0],rect[1]),(rect[0] + rect[2],rect[1]+rect[3]),(0,255,0),2) #draw bounding box for the face
		        cv2.putText(frame,recog_data[i][0]+" - "+str(recog_data[i][1])+"%",(rect[0],rect[1]),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv2.LINE_AA)
		        for rollno, name in names.items():   
		           if name == recog_data[i][0]:
		           	for i in range(1):
		           		vs.release()
		           		cv2.destroyAllWindows()
		           		os.system('python auth1.py')
		           		# vs.release()
		           		# cv2.destroyAllWindows()
						# vs.release() # camera release 
						# cv2.destroyAllWindows() 
		           else:
		               pass 
          
		cv2.imshow("Capturing Face",frame)
		key = cv2.waitKey(1) & 0xFF
		if key == 27 or key == ord("q"):
		    break
	vs.release() # camera release 
	cv2.destroyAllWindows()  

# def releases():
# 	# vs = cv2.VideoCapture(0);
# 	# vs.release()
# 	cv2.destroyAllWindows()

def findPeople(features_arr, positions, thres = 0.6, percent_thres = 70):
    '''
    :param features_arr: a list of 128d Features of all faces on screen
    :param positions: a list of face position types of all faces on screen
    :param thres: distance threshold
    :return: person name and percentage
    '''
    f = open('./master.txt','r');
    data_set = json.loads(f.read());

    returnRes = [];
    for (i,features_128D) in enumerate(features_arr):
        result = "Unknown";
        smallest = sys.maxsize
        for person in data_set.keys():
            person_data = data_set[person][positions[i]];
            for data in person_data:
                distance = np.sqrt(np.sum(np.square(data-features_128D)))
                if(distance < smallest):
                    smallest = distance;
                    result = person;
        percentage =  min(100, 100 * thres / smallest)
        if percentage <= percent_thres :
            result = "Unknown"
        returnRes.append((result,percentage))
    return returnRes

###################################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, help="Run camera recognition", default="camera")
    args = parser.parse_args(sys.argv[1:]);
    FRGraph = FaceRecGraph();
    aligner = AlignCustom();
    extract_feature = FaceFeature(FRGraph)
    face_detect = MTCNNDetect(FRGraph, scale_factor=2); #scale_factor, rescales image for faster detection
    main(args);



                   

