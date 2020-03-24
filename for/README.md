# Attendance-FaceRec
Automating attendance using Face Recognition via Neural Networks 

The entire process of marking attendance in educational institutions, workplaces, when automized is the best and most cost effective way of making it fool-proof and better.

This makes proxy attendance impossible and the workplace ethics- trustworthy

This, while isn't the perfect way, it's an attempt to do something similar

This is an implementation by me using various methods - Via Multi Threaded Cascaded Neural Networks


---Requirements to run the program

1) Numpy
2) Tensorflow
3) Keras and other backend
4) Openpyxl
4) OpenCV
5) Opencv Contribution bindings (Needed. Install via: pip install opencv-contrib-python)

Note: If using any Linux distro (Like Ubuntu) that has preinstalled Python, use python3 instead of python to avoid NameError while using the program

---To Run the Program----

1) Clone the project
2) ~~Change the directort/file locations in Recog, Dupli and Readonly--- It's set to work with my system. IF not changed, there'll be an error: "File not found"~~ Updated. You no longer need to update the links. Just run the required segment of code. Add_New and Recog do the entire work. Rest all the files are used by just the two files.
3) Run Add New.py to add new persons to the dataset
4) Open Recog.py and add your name to  names = {} (line 28) to make your name is in program's attendance register
5) Run Recog.py to mark attendance and finalize
6) Output is obtained as Attendance.xlsx- a read only to make sure further editing is not done
7) Check Attendance.xlsx for sheet name as Today's date(Like Att4, if date is 4). --Previous sheets I used for testing have also been saved and not removed. When using check for latest date. When using multiple times, a random seed is appended to Today's date (like Att42). 






--Video Example-----
[![Video Example for my Attendance usign Face Recognition]](https://www.youtube.com/watch?v=Tl_zw6REpm4 "Face Recognition based Attendance System
")


Credits:
1) To Adrian Rosebrock for OpenCV tutorials
2) Adam Geitgey for Machine Learning Tutorials
3) David Sandberg for MTCNN and inception_resnet skeletons
4) David Vu for Python-Json Interactions
