import cv2
from align_custom import AlignCustom
from face_feature import FaceFeature
from mtcnn_detect import MTCNNDetect
from tf_graph import FaceRecGraph
import openpyxl as xl
import datetime
import time
import argparse
import sys
import json
import numpy as np
import pandas as pd

def main(args):
    mode = args.mode
    if(mode == "input"):
        create_manual_data()
    else:
        raise ValueError("Unimplemented mode")
    
def create_manual_data():
    vs = cv2.VideoCapture(0); #get input from webcam

    print("Please input new user name:\n")
    new_name = input(); #ez python input()
    roll=input("Please enter a desired roll no.\n")
  

    f = open('./facerec_128D.txt','r');
    data_set = json.loads(f.read());
    person_imgs = {"Left" : [], "Right": [], "Center": []};
    person_features = {"Left" : [], "Right": [], "Center": []};
    print("Please start turning slowly. Press 'q' to save and add this new user to the dataset");
    while True:
        _, frame = vs.read();
        rects, landmarks = face_detect.detect_face(frame, 80);  # min face size is set to 80x80
        for (i, rect) in enumerate(rects):
            aligned_frame, pos = aligner.align(160,frame,landmarks[i]);
            if len(aligned_frame) == 160 and len(aligned_frame[0]) == 160:
                person_imgs[pos].append(aligned_frame)
                cv2.imshow("Captured face", aligned_frame)
        key = cv2.waitKey(1) & 0xFF
        if key == 30 or key == ord("q"):
            break


    pre=pd.read_excel('Class.xlsx')
    writer = pd.ExcelWriter('Class.xlsx', engine='xlsxwriter')
    # g = open('./names.txt','r');
    # jso
    # names = {2:'Rishabh'}
    names = json.loads(open('names.txt').read())
    while True:
        y=pre.to_dict()
        yy=y['Names']
        yr=y['Roll Numbers']
        yy.update({len(yy):new_name})
        yr.update({len(yr):roll})
        post=pd.DataFrame(y)
        post.to_excel(writer, sheet_name='Roll', index = False)
        writer.save()
        names.update({(len(names)+2):new_name})
        json.dump(names, open("names.txt",'w'))
        break

    for pos in person_imgs: #there r some exceptions here, but I'll just leave it as this to keep it simple
        person_features[pos] = [np.mean(extract_feature.get_features(person_imgs[pos]),axis=0).tolist()]
    data_set[new_name] = person_features;
    f = open('./facerec_128D.txt', 'w');
    f.write(json.dumps(data_set))


face_detect = None
aligner = None
extract_feature = None
FRGraph = None

# def main_fun():
#     global face_detect, aligner, extract_feature, FRGraph
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--mode", type=str, help="Run camera recognition", default="camera")
#     args = parser.parse_args(sys.argv[1:]);
#     FRGraph = FaceRecGraph();
#     aligner = AlignCustom();
#     extract_feature = FaceFeature(FRGraph)
#     face_detect = MTCNNDetect(FRGraph, scale_factor=2); #scale_factor, rescales image for faster detection
#     main(args);
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, help="Add New Face data", default="input")
    args = parser.parse_args(sys.argv[1:]);
    FRGraph = FaceRecGraph();
    aligner = AlignCustom();
    extract_feature = FaceFeature(FRGraph)
    face_detect = MTCNNDetect(FRGraph, scale_factor=2); #scale_factor, rescales image for faster detection
    main(args);


