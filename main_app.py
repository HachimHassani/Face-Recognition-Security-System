import pickle
from playsound import playsound
import sys
import cv2
import time
import PySide2
from PySide2 import QtWidgets,QtCore,QtGui
from PySide2.QtUiTools import QUiLoader 
from PySide2.QtWidgets import QApplication,QMainWindow 
from PySide2.QtCore import QFile, QIODevice, Qt ,Signal , QThread
import face_recognition as fr
from mainui import mainpasswindow                    
from facerecognition import fr_main
import numpy as np

'''


 _______  _        _______ _________ _______  _______ 
(  ____ \( (    /|(  ____ \\__   __/(  ___  )(  ____ \
| (    \/|  \  ( || (    \/   ) (   | (   ) || (    \/
| (__    |   \ | || (_____    | |   | (___) || (_____ 
|  __)   | (\ \) |(_____  )   | |   |  ___  |(_____  )
| (      | | \   |      ) |   | |   | (   ) |      ) |
| (____/\| )  \  |/\____) |___) (___| )   ( |/\____) |
(_______/|/    )_)\_______)\_______/|/     \|\_______)
                                                      

This package was made as a 1st year's end of year project "face recognition and security system" 
at the National School of computer science (ENSIAS)

'''
def alarm():
    playsound("alarm.mp3")
class safelock:
    def __init__(self) -> None:
        self.password = "1234"
        self.window = None
        self.numoftries = 0
        self.buffer = ""
    def input_num(self,n):
        self.buffer += str(n)
        self.window.password.setText("*"*len(self.buffer))
    def remove_num(self):
        self.buffer = self.buffer[:-1]
        self.window.password.setText("*"*len(self.buffer))
    def is_correct(self):
        k = self.window.thread.get_frame()
        if self.buffer == self.password and k:
            self.window.password.setText("WELCOME !")
        else:
            self.numoftries += 1
            if self.numoftries > 3:
                self.set_alarm()
            self.window.password.setText("NO ENTRY")
    def reset(self):
        self.buffer = ""
    def set_alarm(self):
        alarm()

class VideoThread(QThread):
    '''
    This class is responsible of real time webcam frame's face detection and showing it on the ui 
    '''
    def __init__(self) -> None:
        super().__init__()
        self.cap = cv2.VideoCapture(0)
        self.frs = fr_main()
    change_img = Signal(np.ndarray)
    def get_frame(self):
        time.sleep(3.0)
        while True:
            ret, frame = self.cap.read()
            
            # Detect Faces
            face_locations, face_names = self.frs.detect_known_faces(frame)
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                #cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 3)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (20,200, 200), 6)    
            if ret:
                if name != "":
                    print("yes i found you")
                    return True
                else :
                    return False

    def run(self):
        '''
        this function is executed in runtime of the thread and responsible of the widget's video
        '''
        while True:
            ret, frame = self.cap.read()
            
            # Detect Faces
            face_locations, face_names = self.frs.detect_known_faces(frame)
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                #cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 3)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (20,200, 200), 6)
              
            if ret:
                self.change_img.emit(frame)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = mainpasswindow()
        self.ui.setupUi(self)

    

if __name__ == "__main__":
    lock = safelock()
    t = True
    app = QApplication(sys.argv)
        
    window = MainWindow()
    lock.window = window.ui
    window.show()
    for n in range(2, 11):
            getattr(window.ui, 'pushButton_%s' % n).pressed.connect(lambda v=n: lock.input_num(v-1))
    window.ui.pushButton_11.pressed.connect(lambda:lock.input_num(0))
    window.ui.pushButton_12.pressed.connect(lambda:lock.remove_num())
    window.ui.pushButton.pressed.connect(lambda:lock.is_correct())
    window.ui.thread = VideoThread()
    # connect its signal to the update_image slot
    window.ui.thread.change_img.connect(window.ui.show_image)
    # start the thread
    window.ui.thread.start()
    sys.exit(app.exec_())

    cap.release()	
    cv2.destroyAllWindows()
    cv2.waitKey(0)
    
