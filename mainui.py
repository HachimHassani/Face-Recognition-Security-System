# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import PySide2
from PySide2 import QtWidgets,QtCore,QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import cv2


class DisplayImageWidget(QLabel):
    def __init__(self, parent=None):
        super(DisplayImageWidget, self).__init__(parent)
        pass

    

class mainpasswindow(object):
    
    def __init__(self) -> None:
        self.frame_size = 0.2
        self.img_w = 640
        self.img_h = 480
        self.thread = None
       
        pass
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(628, 565)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 40, 550, 500))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(27, 42, 68, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(40, 63, 102, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(33, 52, 85, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(13, 21, 34, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(18, 28, 45, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush8 = QBrush(QColor(255, 255, 255, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.widget.setPalette(palette)
        self.widget.setStyleSheet(u"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 280, 430))
        self.label.setStyleSheet(u"border-image: url(images/background.png);\n"
"border-top-left-radius: 50px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 30, 321, 430))
        self.label_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius: 50px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 30, 201, 430))
        self.label_3.setStyleSheet(u"background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(330, 90, 151, 40))
        font = QFont()
        font.setFamily(u"Lohit Odia")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color:rgba(0, 0, 0, 200);")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 350, 131, 40))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.pushButton.setPalette(palette1)
        font1 = QFont()
        font1.setFamily(u"Lohit Odia")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 80, 271, 130))
        self.label_6.setStyleSheet(u"background-color:rgba(0, 0, 0, 75);")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 100, 180, 40))
        font2 = QFont()
        font2.setFamily(u"Lohit Odia")
        font2.setPointSize(22)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color:rgba(255, 255, 255, 200);")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 130, 220, 50))
        font3 = QFont()
        font3.setFamily(u"Lohit Odia")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color:rgba(255, 255, 255, 170);")
        self.password = QLabel(self.widget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(360, 140, 111, 20))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush9 = QBrush(QColor(239, 239, 239, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush)
        brush10 = QBrush(QColor(247, 247, 247, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush10)
        brush11 = QBrush(QColor(119, 119, 119, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush11)
        brush12 = QBrush(QColor(159, 159, 159, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush12)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush10)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush13 = QBrush(QColor(0, 0, 0, 128))
        brush13.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush13)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush11)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush12)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush12)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush11)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush13)
#endif
        self.password.setPalette(palette2)
        self.face = QLabel(self.widget)
        self.face.setObjectName(u"face")
        self.face.setGeometry(QtCore.QRect(80, 250, 10+640*self.frame_size, 10+480*self.frame_size))
        self.widget1 = QWidget(self.widget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(320, 170, 181, 156))
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.widget1)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_8 = QPushButton(self.widget1)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 2, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.widget1)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.widget1)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)

        self.gridLayout.addWidget(self.pushButton_4, 0, 2, 1, 1)

        self.pushButton_11 = QPushButton(self.widget1)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFocusPolicy(Qt.StrongFocus)

        self.gridLayout.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget1)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.widget1)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.widget1)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 2, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.widget1)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.widget1)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.widget1)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.widget1)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout.addWidget(self.pushButton_13, 3, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi
    
    # setupUi
    @QtCore.Slot()
    def show_image(self,img):

        
        self.image = img

        #self.image = cv2.resize(self.image, (0, 0), fx=self.frame_size, fy=self.frame_size)
        self.image = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.image = self.image.scaled(self.img_w*self.frame_size, self.img_h*self.frame_size, Qt.KeepAspectRatio)
        self.face.setPixmap(QtGui.QPixmap.fromImage(self.image))
        

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Main", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"ENTER", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"ENSIAS", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Secure face Lock", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"<-", None))
        self.pushButton_13.setText("")
        self.password.setText(QCoreApplication.translate("Form", u"", None))
    # retranslateUi

